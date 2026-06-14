from app import create_app
import threading
import webbrowser
import time

app = create_app()

def open_browser():
    # Wait 2 seconds for server to start then open browser
    time.sleep(2)
    webbrowser.open('http://localhost')

if __name__ == '__main__':
    # Open browser automatically in background thread
    threading.Thread(target=open_browser).start()
    app.run(host='0.0.0.0', port=5000)