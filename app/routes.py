from flask import Blueprint, render_template, jsonify, Response
import platform
import datetime
import psutil
import csv
import io

main = Blueprint('main', __name__)
visit_count = 0

@main.route('/')
def home():
    global visit_count
    visit_count += 1
    return render_template('index.html')

@main.route('/health')
def health():
    return render_template('health.html',
        status='healthy',
        timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        python_version=platform.python_version(),
        system=platform.system()
    )

@main.route('/info')
def info():
    return render_template('info.html',
        app='Dockerized Web Application',
        version='1.0.0',
        intern='Your Name',
        domain='DevOps'
    )

@main.route('/stats')
def stats():
    return render_template('stats.html')

@main.route('/api/stats')
def api_stats():
    global visit_count
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    disk_percent = round((disk.used / disk.total) * 100, 1)
    return jsonify({
        'cpu_percent': cpu,
        'memory_total_mb': round(mem.total / 1024 / 1024),
        'memory_used_mb': round(mem.used / 1024 / 1024),
        'memory_percent': round(mem.percent, 1),
        'disk_used_gb': round(disk.used / 1024 / 1024 / 1024, 2),
        'disk_total_gb': round(disk.total / 1024 / 1024 / 1024, 2),
        'disk_percent': disk_percent,
        'net_bytes_sent': net.bytes_sent,
        'net_bytes_recv': net.bytes_recv,
        'visit_count': visit_count,
        'timestamp': datetime.datetime.now().isoformat()
    })

@main.route('/api/health')
def api_health():
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'uptime_check': 'ok',
        'system': platform.system(),
        'python_version': platform.python_version(),
        'cpu_percent': cpu,
        'memory_percent': round(mem.percent, 1),
        'disk_percent': round((disk.used / disk.total) * 100, 1),
        'visit_count': visit_count
    })

@main.route('/api/processes')
def api_processes():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    top = sorted(procs, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:8]
    return jsonify(top)

@main.route('/api/export')
def export_stats():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    now = datetime.datetime.now().isoformat()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Metric', 'Value', 'Timestamp'])
    writer.writerow(['CPU %', cpu, now])
    writer.writerow(['Memory Used MB', round(mem.used / 1024 / 1024), now])
    writer.writerow(['Memory %', round(mem.percent, 1), now])
    writer.writerow(['Disk Used GB', round(disk.used / 1024 / 1024 / 1024, 2), now])
    writer.writerow(['Disk %', round((disk.used / disk.total) * 100, 1), now])
    writer.writerow(['Net Bytes Sent', net.bytes_sent, now])
    writer.writerow(['Net Bytes Recv', net.bytes_recv, now])
    writer.writerow(['Visit Count', visit_count, now])

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=devops_stats.csv'}
    )