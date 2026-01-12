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
- **Deployment:** Deployment is prepared for cloud platforms such as PythonAnywhere or Render.

- **Version Control:** Git + GitHub

---

## 🧱 Architecture Overview

The API follows a standard layered structure:

- **Models:** Define Users, Projects, Tasks, and Labels
- **Serializers:** Control how models are converted to/from JSON
- **Views / ViewSets:** Implement business logic for each endpoint
- **URLs / Routers:** Map endpoints to views
- **Permissions:** Ensure users can only access their own data
---
### ERD

The ERD is designed using Lucidchart and shows the relationships between:

- User
- Project
- Task
- Label

(ERD link goes here)
- **Link:** https://lucid.app/lucidchart/ace755ef-0c43-430c-a22f-50bf99b89eef/edit?invitationId=inv_796319b0-b798-4ef8-8424-a738a4b9fa64

---


## ⚙️ Installation

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/MinaBG96/Alx_Task_Management_API.git
cd Task_Management_API/Alx_Task_Management_API/Task_Management_API

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```
---
## 🔐 Authentication

This API uses JWT authentication.  
Include the access token in the request header:


* **All protected endpoints require authentication.**

## 🔗 Main API Endpoints
**Detailed API documentation is available in API_DOCUMENTATION.md**

*Auth*
- **POST** /api/auth/register – Register new user
- **POST** /api/auth/login – Obtain JWT access/refresh tokens

*Users*
- **GET** /api/users/me – Get current user info
- **PUT** /api/users/me – Update profile
- **DELETE** /api/users/me – Delete account (optional)*

*Projects*
- **GET**/api/projects – List all user projects
- **POST** /api/projects – Create project
- **GET** /api/projects/{id} – Retrieve single project
- **PUT** /api/projects/{id} – Update project
- **DELETE** /api/projects/{id} – Delete project

*Tasks*
- **GET**/api/tasks – List all tasks for user
- **GET**/api/projects/{projectId}/tasks – List tasks under a project
- **POST** /api/tasks – Create task
- **GET** /api/tasks/{id} – Retrieve single task
- **PUT** /api/tasks/{id} – Update task
- **DELETE** /api/tasks/{id} – Delete task

*Labels*
- **GET** /api/labels – List labels
- **POST** /api/labels – Create label
- **GET** /api/labels/{id} – Retrieve label
- **PUT** /api/labels/{id} – Update label
- **DELETE** /api/labels/{id} – Delete label
- **POST** /api/tasks/{taskId}/labels/{labelId} – Attach label to task
- **DELETE** /api/tasks/{taskId}/labels/{labelId} – Remove label from task





## 👤 Author

- **Name:** Mina Boles
- **GitHub:** https://github.com/MinaBG96
- **LinkedIn:** https://www.linkedin.com/in/mina-boles-406aa22a2/

