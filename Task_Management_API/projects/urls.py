from django.urls import path
from .views import ProjectListCreateAPIView , ProjectDetailAPIView

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view()),
    path('<int:pk>/', ProjectDetailAPIView.as_view()),
]
