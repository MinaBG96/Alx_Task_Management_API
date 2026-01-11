# Main API Endpoints

## Auth

### 1. _register user_

- **POST** /api/auth/register – Register new user
  - _Request Body_
    ```bash
    json{
        "username": "mina1",
        "email": "mina@test.com",
        "password": "1234"
    }
    ```
  - _response_
    ```bash
    json{
        "message": "User registered successfully"
    }
    ```

### 2. _login user_

- **POST** /api/auth/login – Obtain JWT access/refresh tokens
  - _Request Body_
    ```bash
    json{
        "username": "mina1",
        "email": "mina@test.com",
        "password": "1234"
    }
    ```
  - _response_
    ```bash
    json{
        "refresh": "<access-token>",
        "access": "<access-token>"
    }
    ```

## Users

### 1. _Get current user info_

- **GET** /api/users/me – Get current user info
  - _Headers_ :
    1. add key **Authorization**
    2. add value: **Bearer access-token**
  - _Request Body_
    ```bash
    json{
        "username": "mina",
        "email": "mina@test.com"
    }
    ```
  - _Response_
    ```bash
    json{
        "id": 1,
        "username": "mina",
        "email": "mina@test.com"
    }
    ```

### 2. _Update profile_

- **PUT** /api/users/me – Update profile
  - _Headers_ :
    1. add key **Authorization**
    2. add value: **Bearer access-token**
  - _Request Body_
    ```bash
    json{
        "username": "mina_updated",
        "email": "mina_update@test.com"
    }
    ```
  - _Response_
    ```bash
    json{
        "username": "mina_updated",
        "email": "mina_update@test.com"
    }
    ```

### 3. _Delete account_

- **DELETE** /api/users/me/ – Delete account (optional)
  - _Headers_ :
    1. add key **Authorization**
    2. add value: **Bearer access-token**
  - _Request Body_
    ```bash
    json{
        "username": "mina3",
        "email": "mina2@test.com"
    }
    ```
  - _Response_
    ```bash
    json{
        "message": "User account deleted successfully"
    }
    ```

## Projects

### 1. _Create project_

- **POST** /api/projects – Create project
  - _Headers_ :
    1. add key **Authorization of specific user**
    2. add value: **Bearer <_access-token_> of specific user**
  - _Request Body_
    ```bash
    json{
        "name": "My First Project",
        "description": "This is my first project"
    }
    ```
  - _Response_
    ```bash
    json{
        "id": 1,
        "name": "My First Project",
        "description": "This is my first project",
        "created_at": "2026-01-11T21:36:15.003205Z",
        "updated_at": "2026-01-11T21:36:15.003223Z"
    }
    ```

### 2. _List all user projects_

- **GET**/api/projects – List all user projects
  - _Headers_ :
    1. add key **Authorization of specific user**
    2. add value: **Bearer <_access-token_> of specific user**
  - _Response_
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

### 3. _Retrieve single project_

- **GET** /api/projects/{id} – Retrieve single project
  - _Headers_ :
    1. add key **Authorization of specific user**
    2. add value: **Bearer <_access-token_> of specific user**
  - _Response_
    ```bash
    json{
        "id": 1,
        "name": "My First Project",
        "description": "This is my first project",
        "created_at": "2026-01-11T21:36:15.003205Z",
        "updated_at": "2026-01-11T21:36:15.003223Z"
    }
    ```

### 4. _Update project_

- **PUT** /api/projects/{id} – Update project
  - _Headers_ :
    1. add key **Authorization of specific user**
    2. add value: **Bearer <_access-token_> of specific user**
  - _Request Body_
    ```bash
    json{
        "name":"My First Project Updated",
        "description": "This is my first project Updated"
    }
    ```
  - _Response_
    ```bash
    json{
        "id": 1,
        "name": "My First Project Updated",
        "description": "This is my first project Updated",
        "created_at": "2026-01-11T21:36:15.003205Z",
        "updated_at": "2026-01-11T22:00:19.857215Z"
    }
    ```

### 5. _Delete project_

- **DELETE** /api/projects/{id} – Delete project
  - _Headers_ :
    1. add key **Authorization of specific user**
    2. add value: **Bearer <_access-token_> of specific user**
  - _Response_
    ```bash
    json{
        "message": "Project deleted successfully"
    }
    ```

## Tasks

### 1. *Create task*
- **POST** /api/tasks – Create task
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <_access-token_> of specific user**
    * *Request Body* :
        ```bash
        json{
            "title": "First Task",
            "description": "This is my first task",
            "priority": "high",
            "project": 1
        }
        ```
    * *Response* :
        ```bash
        json{
            "id": 1,
            "title": "First Task",
            "description": "This is my first task",
            "is_completed": false,
            "priority": "high",
            "project": 1,
            "created_at": "2026-01-11T22:30:49.327585Z",
            "updated_at": "2026-01-11T22:30:49.327606Z"
        }
### 2. *List all tasks for user*
- **GET**/api/tasks – List all tasks for user
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <_access-token_> of specific user**
    * *Response* :
        ```bash
        json{
                {
                    "id": 1,
                    "title": "First Task",
                    "description": "This is my first task",
                    "is_completed": false,
                    "priority": "high",
                    "project": 1,
                    "created_at": "2026-01-11T22:30:49.327585Z",
                    "updated_at": "2026-01-11T22:30:49.327606Z"
                },
                {
                    "id": 2,
                    "title": "Second Task",
                    "description": "This is my Second task",
                    "is_completed": false,
                    "priority": "high",
                    "project": 1,
                    "created_at": "2026-01-11T22:41:04.647520Z",
                    "updated_at": "2026-01-11T22:41:04.647546Z"
                },
                {
                    "id": 3,
                    "title": "Second Task",
                    "description": "This is my Second task",
                    "is_completed": false,
                    "priority": "high",
                    "project": 1,
                    "created_at": "2026-01-11T22:44:19.920548Z",
                    "updated_at": "2026-01-11T22:44:19.920562Z"
                }
        }
### 3. *Retrieve single task*
- **GET**/api/tasks/{id} – Retrieve single task
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <_access-token_> of specific user**
    * *Response* :
        ```bash
        json{
            "id": 1,
            "title": "First Task",
            "description": "This is my first task",
            "is_completed": false,
            "priority": "high",
            "project": 1,
            "created_at": "2026-01-11T22:30:49.327585Z",
            "updated_at": "2026-01-11T22:30:49.327606Z"
        }
### 4. *List tasks under a project*
- **GET**/api/projects/{projectId}/tasks – List tasks under a project
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <_access-token_> of specific user**
    * *Response* :
        ```bash
        json{
                {
                    "id": 1,
                    "title": "First Task",
                    "description": "This is my first task",
                    "is_completed": false,
                    "priority": "high",
                    "project": 1,
                    "created_at": "2026-01-11T22:30:49.327585Z",
                    "updated_at": "2026-01-11T22:30:49.327606Z"
                },
                {
                    "id": 2,
                    "title": "Second Task",
                    "description": "This is my Second task",
                    "is_completed": false,
                    "priority": "high",
                    "project": 1,
                    "created_at": "2026-01-11T22:41:04.647520Z",
                    "updated_at": "2026-01-11T22:41:04.647546Z"
                },
                {
                    "id": 3,
                    "title": "Second Task",
                    "description": "This is my Second task",
                    "is_completed": false,
                    "priority": "high",
                    "project": 1,
                    "created_at": "2026-01-11T22:44:19.920548Z",
                    "updated_at": "2026-01-11T22:44:19.920562Z"
                }
        }
### 5. *Update task*
- **PUT**/api/tasks/{id} – Update task
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <_access-token_> of specific user**
    * *Request Body*
        ```bash
        json{
            "title":"Third Task",
            "description":"This is my Third task",
            "priority":"high",
            "project": 1
        }
        ```
        * *Response*
        ```bash
        json{
            "id": 3,
            "title": "Third Task",
            "description": "This is my Third task",
            "is_completed": false,
            "priority": "high",
            "project": 1,
            "created_at": "2026-01-11T22:44:19.920548Z",
            "updated_at": "2026-01-11T23:05:45.735466Z"
        }
        ```
### 6. *Delete task*
- **DELETE** /api/tasks/{id} – Delete task
    * *Headers* :
        1. add key **Authorization of specific user**
        2. add value: **Bearer <_access-token_> of specific user**
    * *Response*
        ```bash
        json{
            "message": "Task deleted successfully"
        }

## Labels

- **POST** /api/labels – Create label
- **GET** /api/labels – List labels
- **PUT** /api/labels/{id} – Update label
- **GET** /api/labels/{id} – Retrieve label
- **DELETE** /api/labels/{id} – Delete label
- **POST** /api/tasks/{taskId}/labels/{labelId} – Attach label to task
- **DELETE** /api/tasks/{taskId}/labels/{labelId} – Remove label from task
