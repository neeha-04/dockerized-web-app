# 🐳 Dockerized Web Application

A Flask-based web application containerized using Docker and deployed with Docker Compose, Gunicorn, and Nginx Reverse Proxy. This project demonstrates modern DevOps practices including containerization, deployment, monitoring, and cloud hosting.

---

# 📋 Internship Details

| Field                 | Details                        |
| --------------------- | ------------------------------ |
| **Candidate Name**    | Neeharika Shakthivelan         |
| **Intern ID**         | CITS4308                       |
| **Organization**      | CodTech IT Solutions Pvt. Ltd. |
| **Domain**            | DevOps                         |
| **Project Title**     | Dockerized Web Application     |

---

# 🌐 Live Deployment

### Live Demo

https://dockerized-web-app-7q5e.onrender.com

### Available Endpoints

* Home Page: https://dockerized-web-app-7q5e.onrender.com/
* Health Check: https://dockerized-web-app-7q5e.onrender.com/health
* Application Information: https://dockerized-web-app-7q5e.onrender.com/info
* Statistics Dashboard: https://dockerized-web-app-7q5e.onrender.com/stats

---

# 📖 Project Overview

This project demonstrates how a Flask web application can be containerized using Docker and deployed in a production-ready environment. The application is served through Gunicorn and managed using Docker Compose while Nginx acts as a reverse proxy.

The project provides monitoring capabilities such as health checks, system information, statistics dashboards, and API endpoints that allow users to observe application and system performance.

---

# 🎯 Objectives

* Containerize a web application using Docker.
* Deploy services using Docker Compose.
* Configure Nginx as a reverse proxy.
* Implement production deployment using Gunicorn.
* Monitor application health and system statistics.
* Learn modern DevOps deployment practices.

---

# 🚀 Features

✅ Flask Web Application

✅ Docker Containerization

✅ Docker Compose Orchestration

✅ Nginx Reverse Proxy

✅ Gunicorn Production Server

✅ Health Monitoring

✅ System Statistics Dashboard

✅ Process Monitoring

✅ CSV Export Functionality

✅ Environment Variable Configuration

✅ Cloud Deployment on Render

---

# 🏗️ System Architecture

```text
Client Browser
       │
       ▼
   Nginx Proxy
       │
       ▼
 Flask Application
   (Gunicorn)
       │
       ▼
 Monitoring APIs
```

---

# 🛠️ Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Python 3       | Backend Development     |
| Flask          | Web Framework           |
| Docker         | Containerization        |
| Docker Compose | Container Orchestration |
| Gunicorn       | Production WSGI Server  |
| Nginx          | Reverse Proxy           |
| HTML/CSS       | Frontend Interface      |
| psutil         | System Monitoring       |

---

# 📁 Project Structure

```text
dockerized-web-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│
├── nginx/
│   └── nginx.conf
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
├── .env
├── .dockerignore
├── README.md
└── start.bat
```

---

# ⚙️ Installation and Setup

## Clone Repository

```bash
git clone https://github.com/neeha-04/dockerized-web-app.git
cd dockerized-web-app
```

## Build Docker Image

```bash
docker build -t dockerized-web-app .
```

## Run Using Docker Compose

```bash
docker-compose up --build
```

## Run in Detached Mode

```bash
docker-compose up -d
```

## Stop Containers

```bash
docker-compose down
```

---

# 🌐 API Endpoints

| Endpoint         | Description             |
| ---------------- | ----------------------- |
| `/`              | Home Page               |
| `/health`        | Health Check            |
| `/info`          | Application Information |
| `/stats`         | Statistics Dashboard    |
| `/api/health`    | Health API              |
| `/api/stats`     | Statistics API          |
| `/api/processes` | Running Processes API   |
| `/api/export`    | Export CSV Data         |

---

# 📊 Monitoring Features

### Health Monitoring

* Application Status
* System Status
* Python Version
* Operating System Information

### Statistics Dashboard

* CPU Usage
* Memory Usage
* Disk Usage
* Network Information

### Process Monitoring

* Running Processes
* CPU Utilization
* Memory Utilization
* Process Status

---

# 🔒 Security Features

* Docker Container Isolation
* Reverse Proxy Protection
* Environment Variable Management
* Non-root Container Execution
* Production-grade Gunicorn Deployment

---

# 🐳 Docker Commands

### Build Image

```bash
docker build -t dockerized-web-app .
```

### Run Container

```bash
docker run -p 5000:5000 dockerized-web-app
```

### View Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop <container_id>
```

### Remove Container

```bash
docker rm <container_id>
```

---

# 📚 Learning Outcomes

Through this project, the following skills were developed:

* Docker Fundamentals
* Docker Compose Management
* Container Networking
* Nginx Configuration
* Gunicorn Deployment
* Flask Application Hosting
* Monitoring and Logging
* DevOps Best Practices
* Cloud Deployment
* Production Environment Configuration

---

# ✅ Conclusion

The Dockerized Web Application project successfully demonstrates the deployment of a Flask application using Docker and related DevOps technologies. The project integrates containerization, reverse proxy configuration, monitoring, and cloud deployment to create a scalable and production-ready solution.

This project provided valuable hands-on experience with modern DevOps tools and workflows, strengthening practical knowledge of application deployment and infrastructure management.

---

# 🔗 Project Links

### GitHub Repository

https://github.com/neeha-04/dockerized-web-app

### Live Deployment

https://dockerized-web-app-7q5e.onrender.com

---

# 👩‍💻 Author

**Neeharika Shakthivelan**

DevOps Intern
CodTech IT Solutions Pvt. Ltd.

**Intern ID:** CITS4308

---

## ⭐ Acknowledgement

This project was developed as part of the DevOps Internship Program offered by CodTech IT Solutions Pvt. Ltd. The internship provided practical exposure to Docker, container orchestration, deployment automation, monitoring, and modern DevOps practices.
