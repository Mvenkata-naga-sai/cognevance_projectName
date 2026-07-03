# 🌐 Online Job Portal System

## 📌 Project Overview

The **Online Job Portal System** is a full-stack web application that connects employers and job seekers. Employers can post job openings, and candidates can browse and apply for jobs.

This project is built using:

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Database:** SQLite

---

## 🚀 Features

### 👤 User Authentication

* User Registration
* Login & Logout
* Role-based access (Employer / Candidate)

### 💼 Job Management

* Employers can post jobs
* View all job listings
* Manage job postings

### 📨 Application System

* Candidates can apply for jobs
* Applications stored in database

### 🗄️ Database

* SQLite database (`jobportal.db`)
* Stores users, jobs, and applications

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* SQLite
* Flask-SQLAlchemy

---

## 📂 Project Structure

```id="y2q9gs"
job-portal/
│
├── app.py
├── models.py
├── jobportal.db
├── templates/
│   ├── jobs.html
│   ├── login.html
│   ├── register.html
│   ├── post_job.html
│
├── static/
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Download or Clone Repository

```id="a8p3vx"
git clone https://github.com/your-username/job-portal.git
cd job-portal
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```id="e1k7td"
python -m venv venv
```

Activate:

**Windows:**

```id="q3vnfd"
venv\Scripts\activate
```

**Linux / Mac:**

```id="r5hpz2"
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```id="x7jw2m"
pip install flask flask_sqlalchemy
```

---

### 4️⃣ Run the Application

```id="d9lq4c"
python app.py
```

---

### 5️⃣ Open in Browser

```id="v8k1zr"
http://127.0.0.1:5000/
```

---

## 🔐 User Roles

### 👨‍💼 Employer

* Register as Employer
* Post job openings

### 👨‍🎓 Candidate

* Register as Candidate
* View and apply for jobs

---

## 🗄️ Database Schema

### User Table

* id
* username
* password
* role

### Job Table

* id
* title
* description
* company

### Application Table

* id
* user
* job_id

---

## 📸 Screenshots

(Add after running project)

* Home Page
* Register Page
* Login Page
* Job Listing Page
* Job Posting Page

---

## 🌍 Deployment

You can deploy this project using:

* Render
* Railway
* Heroku

---

## 🎯 Conclusion

This project demonstrates full-stack development using Flask, including authentication, role-based access, job management, and application handling. It is suitable for internships and academic submissions.

---

## 👨‍💻 Author

m venkata naga sai

computer science engineering
