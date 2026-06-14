# 🐳 Dockerized Web Application

> A Flask-based web application containerized using Docker and deployed with Docker Compose and Nginx Reverse Proxy.

---

## 📋 Internship Information

| Field                 | Details                        |
| --------------------- | ------------------------------ |
| **Candidate Name**    | Neeharika Shakthivelan         |
| **Intern ID**         | CITS4308                       |
| **Organization**      | CodTech IT Solutions Pvt. Ltd. |
| **Domain**            | DevOps                         |
| **Project Title**     | Dockerized Web Application     |

---

# 📖 Project Description

This project demonstrates the deployment of a Flask web application using Docker containerization technology. The application is orchestrated using Docker Compose and served through an Nginx reverse proxy. The project follows modern DevOps practices and provides a production-ready environment for deploying web applications.

The application includes monitoring features, health check endpoints, system information APIs, and statistics dashboards that help in tracking application performance and system resource utilization.

---

# 🎯 Objectives

* Containerize a Flask web application using Docker.
* Implement Docker Compose for multi-container orchestration.
* Configure Nginx as a reverse proxy.
* Deploy a production-ready web application using Gunicorn.
* Monitor system performance and application health.
* Learn industry-standard DevOps deployment practices.

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

✅ Secure Non-Root Container Execution

---

# 🏗️ Architecture

```text
┌─────────────────┐
│     Client      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      Nginx      │
│  Reverse Proxy  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Flask + Gunicorn│
│   Application   │
└─────────────────┘
```

---

# 🛠️ Technologies Used

| Technology     | Purpose               |
| -------------- | --------------------- |
| Python 3.11    | Backend Development   |
| Flask          | Web Framework         |
| Docker         | Containerization      |
| Docker Compose | Service Orchestration |
| Nginx          | Reverse Proxy         |
| Gunicorn       | Production Server     |
| HTML/CSS       | Frontend              |
| psutil         | System Monitoring     |

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
├── start.bat
├── RUN_ME.bat
└── README.md
```

---

# ⚙️ Installation and Setup

## Prerequisites

Before running the project, ensure the following software is installed:

* Docker Desktop
* Docker Compose
* Git

---

## Clone Repository

```bash
git clone https://github.com/your-username/dockerized-web-app.git

cd dockerized-web-app
```

---

## Build Docker Image

```bash
docker build -t dockerized-web-app .
```

---

## Run Using Docker Compose

```bash
docker-compose up --build
```

---

## Run in Detached Mode

```bash
docker-compose up -d --build
```

---

## Stop Containers

```bash
docker-compose down
```

---

## View Running Containers

```bash
docker ps
```

---

# 🌐 Application Endpoints

| Endpoint         | Description             |
| ---------------- | ----------------------- |
| `/`              | Home Page               |
| `/health`        | Health Check            |
| `/info`          | Application Information |
| `/stats`         | Statistics Dashboard    |
| `/api/health`    | Health API              |
| `/api/stats`     | System Statistics API   |
| `/api/processes` | Running Processes API   |
| `/api/export`    | Export Statistics CSV   |

---

# 📊 Monitoring Features

## Health Monitoring

* Application Status
* Docker Status
* Python Version
* Operating System Information

## System Statistics

* CPU Usage
* Memory Usage
* Disk Utilization
* Network Information

## Process Monitoring

* Running Processes
* CPU Consumption
* Memory Consumption
* Process Status

---

# 🔒 Security Features

* Non-root Docker Containers
* Nginx Reverse Proxy
* Environment Variable Management
* Gunicorn Production Server
* Docker Network Isolation

---

# 🐳 Docker Commands

## Build Image

```bash
docker build -t dockerized-web-app .
```

## Run Container

```bash
docker run -p 5000:5000 dockerized-web-app
```

## List Containers

```bash
docker ps
```

## Stop Container

```bash
docker stop <container_id>
```

## Remove Container

```bash
docker rm <container_id>
```

## Remove Image

```bash
docker rmi dockerized-web-app
```


# 📚 Learning Outcomes

Through this project, the following concepts were learned:

* Docker Fundamentals
* Containerization Techniques
* Docker Compose
* Reverse Proxy Configuration
* Nginx Administration
* Production Deployment
* Flask Application Deployment
* DevOps Best Practices
* Monitoring and Logging
* Container Networking

---

# ✅ Conclusion

The Dockerized Web Application project successfully demonstrates the implementation of containerization using Docker and service orchestration using Docker Compose. By integrating Flask, Gunicorn, and Nginx, the project provides a scalable and production-ready deployment environment.

This project helped in gaining hands-on experience with modern DevOps tools and practices including application deployment, container management, reverse proxy configuration, and system monitoring.

---

# 👩‍💻 Author

**Neeharika Shakthivelan**

DevOps Intern
CodTech IT Solutions Pvt. Ltd.

**Intern ID:** CITS4308

---

## ⭐ Acknowledgement

This project was developed as part of the DevOps Internship Program offered by CodTech IT Solutions Pvt. Ltd. The internship provided practical exposure to modern DevOps tools, containerization technologies, deployment strategies, and industry best practices.
