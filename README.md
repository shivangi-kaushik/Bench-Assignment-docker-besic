# Simple Flask Application

A simple Flask web application containerized using Docker and Docker Compose.

---

# Project Structure

```bash
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── templates
    └── index.html
```

---

# Application Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Loads the homepage |
| `/health` | Health check API |

---

# Prerequisites

Make sure the following tools are installed:

- Docker
- Docker Compose
- Git

---

# Clone Repository

```bash
git clone <your-github-repository-url>
cd <repository-name>
```

---

# Run Application Using Docker CLI

## Step 1: Build Docker Image

```bash
docker build -t flask-app .
```

## Step 2: Run Docker Container

```bash
docker run -d \
--name flask-container \
-p 5000:5000 \
flask-app
```

## Step 3: Verify Running Containers

```bash
docker ps
```

## Step 4: Access Application

Application:

```bash
http://localhost:5000
```

Health API:

```bash
http://localhost:5000/health
```

---

# Run Application Using Docker Compose

## Step 1: Start Application

```bash
docker compose up -d
```

## Step 2: Verify Containers

```bash
docker compose ps
```

## Step 3: Access Application

```bash
http://localhost:5000
```

---

# Stop Application

## Docker CLI

```bash
docker stop flask-container
docker rm flask-container
```

## Docker Compose

```bash
docker compose down
```

---

# Pull Docker Image From Docker Hub

## Step 1: Login to Docker Hub

```bash
docker login
```

Enter:

- Docker Hub Username
- Docker Hub Password

---

## Step 2: Pull Image

```bash
docker pull <dockerhub-username>/flask-app:latest
```

Example:

```bash
docker pull shivangikaushik/flask-app:latest
```

---

## Step 3: Run Pulled Image

```bash
docker run -d \
--name flask-container \
-p 5000:5000 \
<dockerhub-username>/flask-app:latest
```

---

# Push Docker Image To Docker Hub

## Tag Docker Image

```bash
docker tag flask-app <dockerhub-username>/flask-app:latest
```

## Push Image

```bash
docker push <dockerhub-username>/flask-app:latest
```

---

# Useful Docker Commands

## View Running Containers

```bash
docker ps
```

## View All Containers

```bash
docker ps -a
```

## View Logs

```bash
docker logs flask-container
```

## Remove Docker Image

```bash
docker rmi flask-app
```

---

# Technologies Used

- Python
- Flask
- Docker
- Docker Compose

---

# Author

Shivangi Kaushik
