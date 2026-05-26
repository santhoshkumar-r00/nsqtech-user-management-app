# NSQTech Internship Code Challenge

## 🚀 Project Overview
This project is a full-stack Single Page Application (SPA) developed as part of the NSQTech Software Engineer Intern assignment.

It demonstrates authentication, role-based access control, admin user management, API integration, and asynchronous processing.

---

## 🛠️ Tech Stack

### Frontend
- React
- Axios
- Bootstrap

### Backend
- Django
- Django REST Framework

---

## 🔐 Features

### 1. Login System
- User can login with:
  - Username
  - Password
  - Role (Admin / General User)
- Dummy authentication API implemented

---

### 2. Role-Based Access

#### Admin:
- Add new users
- Delete users
- View all users

#### General User:
- View only (no edit/delete access)

---

### 3. Dashboard
- Displays logged-in user details
- Shows list of users from API
- Shows records table from API

---

### 4. Records Module
- Displays sample records:
  - Employee Data
  - Salary Report
  - HR Documents

---

### 5. Async API Handling (Important Requirement)
- Backend uses:
  - `time.sleep()` to simulate delay
- API supports delay parameter:
  - Example: `/api/users/?delay=3`
- Frontend shows:
  - Loading spinner during API call

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | `/api/login/` | User login |
| GET | `/api/users/` | Get all users |
| POST | `/api/add/` | Add user (Admin only) |
| DELETE | `/api/delete/{id}/` | Delete user |
| GET | `/api/records/` | Get records |

---

## 🧠 Key Highlights

- Role-based authentication system
- REST API using Django
- Async API simulation using delay parameter
- Admin panel for user management
- Modular code structure
- Responsive UI using Bootstrap
- SPA architecture using React

---

## 📁 Project Structure
project/
|-- frontend/
|    |--src/
|    |--pages/
|    |--component/
|    |--services/
|
|-- backend/
|-- api/
|-- models.py
|-- views.py
|-- urls.py

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py runserver
```

##Create Dummy Users
python manage.py shell

from api.models import User

User.objects.create(username="admin", password="123", role="Admin")
User.objects.create(username="user", password="123", role="General User")

##Frontend Setup
cd frontend
npm install
npm start

##📸 Screenshots
### 🔐 Login Page
<img width="359" height="304" alt="login" src="https://github.com/user-attachments/assets/f68a3a96-475a-4d86-bf9e-9fa5ef5237f7" />

### 👨‍💼 Admin Panel
<img width="938" height="440" alt="admin" src="https://github.com/user-attachments/assets/57c1b8c5-6e32-4135-a5c7-0487eb48ccaf" />

### 🔐 Login Page
<img width="368" height="298" alt="Screenshot 2026-05-26 192838" src="https://github.com/user-attachments/assets/b5a0496f-53ca-486b-9db9-7c02dc46b9ea" />

### 📊 Dashboard
<img width="950" height="436" alt="user" src="https://github.com/user-attachments/assets/4078906b-508d-4f1b-9327-43b3dc9c67f3" />
