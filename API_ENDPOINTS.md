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
### 1. *Create project*
- **POST** /api/projects – Create project
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <*access-token*> of specific user**
    * *Request Body*
        ```bash
        json{
            "name": "My First Project",
            "description": "This is my first project"
        }
        ```
    * *Response*
        ```bash
        json{
            "id": 1,
            "name": "My First Project",
            "description": "This is my first project",
            "created_at": "2026-01-11T21:36:15.003205Z",
            "updated_at": "2026-01-11T21:36:15.003223Z"
        }
        ```
### 2. *List all user projects*
- **GET**/api/projects – List all user projects
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <*access-token*> of specific user**
    * *Response*
        ```bash
        json[
            {
                "id": 1,
                "name": "My First Project",
                "description": "This is my first project",
                "created_at": "2026-01-11T21:36:15.003205Z",
                "updated_at": "2026-01-11T21:36:15.003223Z"
            },
            {
                "id": 2,
                "name": "My second Project",
                "description": "This is my second project",
                "created_at": "2026-01-11T21:46:17.813960Z",
                "updated_at": "2026-01-11T21:46:17.813976Z"
            }
        ]
        ```
### 3. *Retrieve single project*
- **GET** /api/projects/{id} – Retrieve single project
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <*access-token*> of specific user**
    * *Response*
        ```bash
        json{
            "id": 1,
            "name": "My First Project",
            "description": "This is my first project",
            "created_at": "2026-01-11T21:36:15.003205Z",
            "updated_at": "2026-01-11T21:36:15.003223Z"
        }
        ```
### 4. *Update project*
- **PUT** /api/projects/{id} – Update project
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <*access-token*> of specific user**
    * *Request Body*
        ```bash
        json{
            "name":"My First Project Updated",
            "description": "This is my first project Updated"
        }
        ```
    * *Response*
        ```bash
        json{
            "id": 1,
            "name": "My First Project Updated",
            "description": "This is my first project Updated",
            "created_at": "2026-01-11T21:36:15.003205Z",
            "updated_at": "2026-01-11T22:00:19.857215Z"
        }
        ```
### 5. *Delete project*
- **DELETE** /api/projects/{id} – Delete project
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <*access-token*> of specific user**
    * *Response*
        ```bash
        json{
            "message": "Project deleted successfully"
        }
        ```
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
