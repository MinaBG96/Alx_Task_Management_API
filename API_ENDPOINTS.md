🔗 Main API Endpoints
Auth

POST /api/auth/register – Register new user

POST /api/auth/login – Obtain JWT access/refresh tokens

Users

GET /api/users/me – Get current user info

PUT /api/users/me – Update profile

DELETE /api/users/me – Delete account (optional)

Projects

GET /api/projects – List all user projects

POST /api/projects – Create project

GET /api/projects/{id} – Retrieve single project

PUT /api/projects/{id} – Update project

DELETE /api/projects/{id} – Delete project

Tasks

GET /api/tasks – List all tasks for user

GET /api/projects/{projectId}/tasks – List tasks under a project

POST /api/tasks – Create task

GET /api/tasks/{id} – Retrieve single task

PUT /api/tasks/{id} – Update task

DELETE /api/tasks/{id} – Delete task

Labels

GET /api/labels – List labels

POST /api/labels – Create label

GET /api/labels/{id} – Retrieve label

PUT /api/labels/{id} – Update label

DELETE /api/labels/{id} – Delete label

POST /api/tasks/{taskId}/labels/{labelId} – Attach label to task

DELETE /api/tasks/{taskId}/labels/{labelId} – Remove label from task
