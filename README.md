# Cloud-Native Data Processing & Observability Platform

A production-style DevOps/SRE project demonstrating cloud-native application deployment, infrastructure automation, CI/CD, monitoring, observability, and alerting on AWS.

---

## 🚀 Overview

This project processes uploaded CSV files using FastAPI, stores processed data in PostgreSQL, and provides end-to-end observability through Prometheus and Grafana.

The infrastructure is provisioned using Terraform, containerized using Docker, deployed on AWS EC2 through GitHub Actions CI/CD, and exposed through an Nginx reverse proxy.

---

## 🏗️ Architecture

```text
                    ┌──────────────┐
                    │    User      │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Nginx     │
                    │ Reverse Proxy│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   FastAPI    │
                    │ Application  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ PostgreSQL   │
                    │  Database    │
                    └──────────────┘


                    ┌──────────────┐
                    │ Prometheus   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Grafana    │
                    └──────────────┘


GitHub Push
     │
     ▼
GitHub Actions
     │
     ▼
AWS EC2 Deployment
```

---

## 🛠️ Tech Stack

### Application

- Python
- FastAPI
- Pandas

### Database

- PostgreSQL

### Containerization

- Docker
- Docker Compose

### Infrastructure

- Terraform
- AWS EC2

### CI/CD

- GitHub Actions

### Networking

- Nginx Reverse Proxy

### Monitoring & Observability

- Prometheus
- Grafana

---

## ✨ Features

- CSV file upload and processing
- PostgreSQL data persistence
- Dockerized microservice architecture
- Infrastructure as Code using Terraform
- Automated deployment using GitHub Actions
- Nginx reverse proxy configuration
- Prometheus metrics collection
- Grafana dashboards
- Custom business metric tracking
- Application health monitoring
- Prometheus alert rules

---

## 📡 API Endpoints

### Upload File

```http
POST /upload
```

Processes uploaded CSV files and stores results in PostgreSQL.

### API Documentation

```http
GET /docs
```

Swagger UI generated automatically by FastAPI.

### Metrics Endpoint

```http
GET /metrics
```

Exposes Prometheus metrics.

---

## 📊 Monitoring

Prometheus scrapes metrics from:

```text
/api/metrics
```

Key metrics monitored:

### Application Metrics

- Total HTTP requests
- Request latency
- Request rate

### Business Metrics

- `files_uploaded_total`

---

## 🚨 Alerting

Prometheus alert rule:

```yaml
alert: FastAPIDown
expr: up{job="fastapi"} == 0
for: 1m
```

Triggers when FastAPI becomes unavailable for more than one minute.

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers an automated deployment.

### Deployment Flow

```text
Developer
   │
   ▼
Git Push
   │
   ▼
GitHub Actions
   │
   ▼
SSH into EC2
   │
   ▼
Pull Latest Code
   │
   ▼
Docker Build
   │
   ▼
Docker Compose Deployment
```

---

## 💾 Persistence Strategy

The project uses Docker volumes for persistent storage.

### PostgreSQL

```text
postgres_data
```

Persists database records across container restarts.

### Grafana

```text
grafana_data
```

Persists dashboards and datasource configurations.

### Prometheus

```text
prometheus_data
```

Persists historical metrics and time-series data.

---

## ☁️ Infrastructure Provisioned Using Terraform

- AWS EC2 Instance
- Security Group
- SSH Key Pair
- EBS Storage

---

## ▶️ Local Development

### Clone Repository

```bash
git clone https://github.com/<your-username>/cloud-native-data-processing-platform.git
cd cloud-native-data-processing-platform
```

### Create Environment File

```env
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=dataplatform
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
```

### Start Application

```bash
docker compose up -d
```

### Access Services

FastAPI:

```text
http://localhost/docs
```

Grafana:

```text
http://localhost:3000
```

Prometheus:

```text
http://localhost:9090
```

---

## 📚 Key DevOps & SRE Concepts Demonstrated

- Infrastructure as Code (Terraform)
- Containerization (Docker)
- Multi-container orchestration (Docker Compose)
- Reverse Proxy Configuration (Nginx)
- CI/CD Automation (GitHub Actions)
- Cloud Infrastructure (AWS EC2)
- Observability (Prometheus & Grafana)
- Custom Metrics
- Alerting
- Persistent Storage with Docker Volumes
- Infrastructure Monitoring

---

## 🔮 Future Enhancements

- HTTPS using Let's Encrypt
- Alertmanager email notifications
- AWS RDS migration
- Kubernetes deployment
- AI-powered log analysis
- Automated backups
- Blue-Green deployments

---

## 👩‍💻 Author

**Sakshi Pande**

DevOps | SRE | Cloud Engineering | Platform Engineering