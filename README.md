# 🛠️ Garage Pro - Management System

A professional, end-to-end Garage Management System (CRUD) built with Python, Flask, and PostgreSQL.

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## 📖 Overview
This project was developed as a comprehensive homework assignment for the John Bryce Programming Course. It demonstrates a full-stack CRUD application for managing a vehicle garage.

### Key Features
*   **Create**: Add new vehicles with owner details and license plate numbers.
*   **Read**: Real-time dashboard showing all vehicles in the garage.
*   **Update**: Change vehicle status (Pending → In Progress → Ready).
*   **Delete**: Release vehicles from the system.
*   **Responsive UI**: Fully mobile-friendly design using Bootstrap 5.

## 🚀 Tech Stack
*   **Backend**: Python / Flask
*   **Database**: PostgreSQL (Relational)
*   **Frontend**: Jinja2 Templates & Bootstrap 5
*   **DevOps**: Docker & Docker Compose
*   **Deployment**: Render (Cloud)

## 🛠️ How to Run Locally

### Using Docker (Easiest)
1. Make sure Docker Desktop is running.
2. Run the provided script:
   ```powershell
   .\run.bat
   ```
   *Or manually:* `docker-compose up --build`
3. Access the site at: `http://localhost:5000`

## ☁️ Deployment
This project is configured for one-click deployment to **Render** using the `render.yaml` blueprint.

---
**Developed by Omri** | John Bryce Course 2026
