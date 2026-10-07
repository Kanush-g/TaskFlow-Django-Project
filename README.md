# 📋 TaskFlow – Django Task Management System

A simple and user-friendly **Task Management Web Application** built using **Python and Django**. TaskFlow helps users organize their tasks, track their progress, set priorities, and manage deadlines.

## ✨ Features

- ➕ Add new tasks
- 👀 View all tasks
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- ✅ Mark tasks as completed
- 🔴 Track pending tasks
- 🏷️ Task categories
- ⭐ Low, Medium, and High priority
- 📅 Due dates
- 📊 Dashboard statistics
- 🎉 Celebration effect when all tasks are completed
- 🎨 Custom HTML and CSS user interface
- 🛠️ Django Admin panel
- 💾 SQLite database

## 🛠️ Technologies Used

- **Python** – Backend programming
- **Django** – Web framework
- **HTML5** – Page structure
- **CSS3** – Styling and design
- **SQLite** – Database
- **Git & GitHub** – Version control and project hosting

## 📁 Project Structure

```text
TaskFlow-Django-Project/
│
├── taskflow/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── add_task.html
│   │       ├── edit_task.html
│   │       └── delete_task.html
│   │
│   ├── static/
│   │   └── tasks/
│   │       └── style.css
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Kanush-g/TaskFlow-Django-Project.git
cd TaskFlow-Django-Project
```

### 2. Create a virtual environment

```bash
python -m venv env_site
```

### 3. Activate the virtual environment

For Windows CMD:

```cmd
env_site\Scripts\activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔐 Django Admin

The Django Admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

The admin panel allows the administrator to manage task records and database data.

## 🗄️ Database

TaskFlow uses **SQLite** as its database.

The `Task` model stores information such as:

- Title
- Description
- Category
- Priority
- Due date
- Completion status
- Created date
- Updated date

## 🔄 Application Flow

TaskFlow follows Django's **Model-View-Template (MVT)** architecture.

```text
User
  ↓
URL
  ↓
View
  ↓
Model / Database
  ↓
View
  ↓
Template
  ↓
Browser
```

### Model

The `Task` model defines the structure of the task and stores task information in the database.

### View

Views handle the application logic, retrieve tasks from the database, update their status, and process add, edit, and delete operations.

### URL

URL patterns connect website URLs to their corresponding views.

### Template

HTML templates display the task information and provide the user interface.

## 📊 Dashboard

The dashboard displays:

- Total number of tasks
- Completed tasks
- Pending tasks
- High-priority tasks

The statistics are automatically calculated from the database.

## 🎯 Project Objective

The objective of this project is to understand the fundamentals of Django development, including:

- Django project and app structure
- Models and databases
- URL routing
- Views
- Templates
- Forms
- CRUD operations
- Database migrations
- Static files and CSS
- Django Admin
- Git and GitHub

## 🔮 Future Improvements

Possible future improvements include:

- User login and authentication
- User-specific task lists
- Search and filtering
- Task sorting
- Notifications and reminders
- Improved mobile responsiveness
- Dark mode

## 👨‍💻 Author

Developed as a college Django project.

**GitHub:**  
https://github.com/Kanush-g/TaskFlow-Django-Project
