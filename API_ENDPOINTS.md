# Main API Endpoints

## Auth
### 1. *register user*
- **POST** /api/auth/register – Register new user
    * *Request Body*
        ```bash
        json{
            "username": "mina1",
            "email": "mina@test.com",
            "password": "1234"
        }
        ```
    * *response*
        ```bash
        json{
            "message": "User registered successfully"
        }
        ```
### 2. *login user*
- **POST** /api/auth/login – Obtain JWT access/refresh tokens
    * *Request Body*
        ```bash
        json{
            "username": "mina1",
            "email": "mina@test.com",
            "password": "1234"
        }
        ```
    * *response*
        ```bash
        json{
            "refresh": "<access-token>",
            "access": "<access-token>"
        }
        ```

## Users
### 1. *Get current user info*
- **GET** /api/users/me – Get current user info
    * *Headers* :
        1. add key **Authorization**
        2. add value: **Bearer access-token**
    * *Request Body*
        ```bash
        json{
            "username": "mina",
            "email": "mina@test.com"
        }
        ```
    * *Response*
        ```bash
        json{
            "id": 1,
            "username": "mina",
            "email": "mina@test.com"
        }
        ```
### 2. *Update profile*
- **PUT** /api/users/me – Update profile
    * *Headers* :
        1. add key **Authorization**
        2. add value: **Bearer access-token**
    * *Request Body*
        ```bash
        json{
            "username": "mina_updated",
            "email": "mina_update@test.com"
        }
        ```
    * *Response*
        ```bash
        json{
            "username": "mina_updated",
            "email": "mina_update@test.com"
        }
        ```
### 3. *Delete account*
- **DELETE** /api/users/me/ – Delete account (optional)
    * *Headers* :
        1. add key **Authorization**
        2. add value: **Bearer access-token**
    * *Request Body*
        ```bash
        json{
            "username": "mina3",
            "email": "mina2@test.com"
        }
        ```
    * *Response*
        ```bash
        json{
            "message": "User account deleted successfully"
        }
        ```

## Projects
- **GET**/api/projects – List all user projects
- **POST** /api/projects – Create project
- **GET** /api/projects/{id} – Retrieve single project
- **PUT** /api/projects/{id} – Update project
- **DELETE** /api/projects/{id} – Delete project

## Tasks
- **GET**/api/tasks – List all tasks for user
- **GET**/api/projects/{projectId}/tasks – List tasks under a project
- **POST** /api/tasks – Create task
- **GET**/api/tasks/{id} – Retrieve single task
- **PUT**/api/tasks/{id} – Update task
- **DELETE** /api/tasks/{id} – Delete task

## Labels
- **GET** /api/labels – List labels
- **POST** /api/labels – Create label
- **GET** /api/labels/{id} – Retrieve label
- **PUT** /api/labels/{id} – Update label
- **DELETE** /api/labels/{id} – Delete label
- **POST** /api/tasks/{taskId}/labels/{labelId} – Attach label to task
- **DELETE** /api/tasks/{taskId}/labels/{labelId} – Remove label from task
