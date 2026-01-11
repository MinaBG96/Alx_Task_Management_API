from django.urls import path
from .views import TaskListCreateAPIView , TaskDetailAPIView , ProjectTasksAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view()),
    path('<int:pk>/', TaskDetailAPIView.as_view()),
    path('projects/<int:project_id>/', ProjectTasksAPIView.as_view()),
]
