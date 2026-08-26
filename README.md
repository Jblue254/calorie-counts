# Calorie Counter

### *Track Every Bite. Stay Healthy.*

---

## About Calorie Counter

**Calorie Counter** is a modern web-based calorie tracking application developed using **Django**, **PostgreSQL**, **Tailwind CSS**, and **Chart.js**. The system helps users monitor their daily food intake by recording meals, calculating calories consumed, visualizing calorie trends, and managing daily nutrition records efficiently.

The application provides an easy-to-use interface for adding food items, tracking calorie consumption, deleting unwanted entries, resetting daily records, and viewing calorie statistics through graphical charts.

---

# Our Motto

## *Track Every Bite. Stay Healthy.*

Healthy living begins with awareness. The Calorie Counter helps users understand their eating habits by keeping track of calories consumed throughout the day.

---

# Mission

To provide a simple and efficient platform that enables users to monitor their daily calorie intake and maintain healthy eating habits through data-driven insights.

---

# Problem Statement

Many people struggle to monitor their daily calorie intake due to the lack of simple and accessible tracking tools. Manual tracking methods often result in:

- Inaccurate calorie records
- Poor dietary monitoring
- Difficulty achieving fitness goals
- Lack of nutritional awareness
- Loss of food consumption records
- Limited visualization of calorie trends

The Calorie Counter was developed to address these challenges by providing a centralized platform for recording and managing daily calorie consumption.

---

# Live Demo

### Visit Calorie Counter

Explore the application and track your daily calorie intake online.

**Live URL:**

```
https://your-render-link.onrender.com
```
---

# Objectives

## Main Objective

To develop a web-based calorie tracking system that helps users monitor and manage their daily calorie consumption effectively.

## Specific Objectives

- To allow users to record food items consumed.
- To calculate the total calories consumed per day.
- To provide graphical visualization of calorie consumption.
- To allow users to delete food records.
- To provide a daily reset functionality.
- To maintain accurate nutritional records using a database.
- To provide an administrative interface for managing calorie records.

---

# Key Features

## User Features

- Add food items
- Record calories consumed
- Track meals by day
- View food history
- Delete food entries
- Reset daily calorie records
- Calculate total calories automatically
- Daily calorie goal tracking
- Progress bar visualization
- Interactive calorie charts

---

## Admin Features

- Secure Django Admin Dashboard
- Food Item Management
- Record Monitoring
- Search Food Records
- Filter Records by Day and Meal
- Database Management

---

# Pages

## Public Pages

* Home Page
* Calorie Tracking Dashboard

---

## Administrative Pages

* Admin Login
* Food Records Management
* Search & Filter Records

---

# Calorie Tracking

Users can record food consumption by entering:

* Day
* Meal Type
* Food Name
* Calories Consumed

The system automatically:

* Stores the information
* Calculates total calories
* Updates charts
* Tracks progress toward calorie goals

---

# Calorie Analytics

The application provides graphical insights through **Chart.js**.

### Available Analytics

* Calorie Consumption Chart
* Daily Intake Visualization
* Progress Tracking
* Goal Monitoring

---

# Daily Goal Tracking

Users can monitor progress toward a predefined calorie goal.

Features include:

* Total Calories Consumed
* Daily Goal Display
* Progress Bar
* Percentage Completion

---

# Authentication

### Administrator

Administrators can:

* Login securely
* Manage food records
* Delete records
* Search entries
* Monitor calorie data
* Manage database content

---

# Tech Stack

| **Technology** |
|----------------|
| Python |
| Django |
| PostgreSQL |
| Tailwind CSS |
| Chart.js |
| HTML5 |
| CSS3 |
| JavaScript |
| Git |
| Render |

---

# Project Structure

```text
CALORIE-COUNTER/
│
├── calorie_tracker/
│   ├── migrations/
│   ├── templates/
│   │   └── calorie_tracker/
│   │       ├── base.html
│   │       └── index.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3
```

---

# Database Design

## Food Item

Each food entry contains:

* Day
* Meal Type
* Food Name
* Calories
* Date Created

---

# Getting Started

## Clone the Repository

```bash
git clone https://github.com/Jblue254/calorie-counter.git
```

---

## Navigate to the Project

```bash
cd calorie-counter
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# Future Improvements

* User Authentication
* Multiple User Accounts
* Meal Categories Expansion
* Nutritional Information Tracking
* Weekly Reports
* Monthly Reports
* PDF Export
* Email Notifications
* Fitness Goal Recommendations
* Mobile Application Version

---

# Deployment

The project is deployed using **Render**.

### Deployment Steps

1. Push project to GitHub.
2. Create a PostgreSQL database on Render.
3. Create a Web Service.
4. Connect GitHub repository.
5. Configure environment variables.
6. Deploy application.
7. Add deployment URL to README.

---

# How to Contribute

Contributions are always welcome!

1. Fork the repository.
2. Clone your fork locally.
3. Create a feature branch.
4. Make your changes.
5. Test your changes thoroughly.
6. Commit with descriptive messages.
7. Push to GitHub.
8. Open a Pull Request.

Please ensure your code follows project standards and does not introduce breaking changes.

---

# License

This project is licensed under the **MIT License**.

---

# Author

**Japheth Kiprono Rotich**

GitHub: https://github.com/Jblue254

---

# Calorie Counter

### *Track Every Bite. Stay Healthy.*
