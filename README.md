# 🐳 Docker & Kubernetes Learning Lab

This repository tracks my hands-on journey to mastering **Docker** and **Kubernetes** through real-world mini-projects.  
Each folder demonstrates a different concept — from containerizing Python apps to orchestrating multi-container environments.

---

## 📁 Project Structure
Docker&K8S/
├── Flask-Api/
│ ├── api/
│ │ ├── main.py
│ │ ├── test_main.py
│ │ ├── requirements.txt
│ │ └── Dockerfile
│ └── docker-compose.yaml
│
├── Nginx+StaticSite/
│ ├── index.html
│ └── Dockerfile
│
├── VisitorCounter/
│ ├── main.py
│ ├── requirements.txt
│ ├── Dockerfile
│ ├── docker-compose.yaml
│ ├── static/
│ └── templates/
│
└── Wordpress/
└── docker-compose.yaml


---

## 🧩 **Projects Overview**

### 🧱 **1. Flask-API**
A simple Python REST API built with **Flask**, containerized with Docker.  
- Demonstrates building lightweight backend images  
- Includes unit tests (`pytest`) and dependency management  

**Run:**
```bash
docker compose up --build



🌐 2. Nginx + Static Site

A minimal static website served via Nginx.

Shows how to serve HTML/CSS with Nginx
Perfect for understanding web server containers

Run:
~~~bash
docker build -t static-site .
docker run -d -p 8080:80 static-site
~~~


👥 3. Visitor Counter (Flask App)

A small Flask application that counts and displays the number of visitors.

Uses Flask templating with Jinja2
Demonstrates Docker volumes & persistence
Built for hands-on Compose practice

Run:

~~~bash
docker compose up --build
~~~

Then open 👉 http://localhost:8080


📰 4. WordPress + MySQL Stack

Full multi-container setup for WordPress backed by MySQL.

Uses Docker Compose
Includes persistent named volumes
Demonstrates healthchecks and inter-container networking

Run:

~~~bash
docker compose up -d
~~~

Then visit 👉 http://localhost:8080


🧠 Tech Stack
  🐍 Python (Flask)
  🐳 Docker & Docker Compose
  ☸️ Kubernetes (up next)
  🌐 Nginx
  🗄️ MySQL / WordPress



  ✨ Author

Ashab Tariq
“Learning by building — one container at a time.”