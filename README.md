# Task Management API

A backend RESTful API for managing projects, tasks, and labels.  
Users can register, log in, create projects, add tasks under projects, organize them with labels, and filter their work efficiently.

This project is built as a capstone project for the ALX Backend program.

---

## 🚀 Features

### Authentication & Users
- User registration (sign up)
- User login (JWT-based authentication)
- View current user profile
- Update profile data
- Delete account (optional)

### Projects
- Create a new project
- List all projects for the logged-in user
- Retrieve a single project
- Update a project
- Delete a project

### Tasks
- Create a task
- List all tasks for the logged-in user
- List tasks under a specific project
- Retrieve a single task
- Update a task
- Delete a task
- Mark task as completed / not completed
- Filter tasks by:
  - Status (completed / not completed)
  - Priority (low / medium / high)
  - Due date (optional extension)

### Labels
- Create a label
- List all labels
- Retrieve a single label
- Update a label
- Delete a label
- Attach / remove labels from tasks

---

## 🛠 Tech Stack

- **Backend Framework:** Django, Django REST Framework (DRF)
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (dev) / PostgreSQL (production-ready)
- **Tools:** Postman / Thunder Client for testing
- **Deployment:** PythonAnywhere / Render
- **Version Control:** Git + GitHub

---

## 🧱 Architecture Overview

The API follows a standard layered structure:

- **Models:** Define Users, Projects, Tasks, and Labels
- **Serializers:** Control how models are converted to/from JSON
- **Views / ViewSets:** Implement business logic for each endpoint
- **URLs / Routers:** Map endpoints to views
- **Permissions:** Ensure users can only access their own data

### ERD

The ERD is designed using Lucidchart and shows the relationships between:
- User
- Project
- Task
- Label

(ERD link goes here)

---


