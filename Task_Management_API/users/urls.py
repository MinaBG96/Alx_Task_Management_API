from django.urls import path
from .views import RegisterAPIView , UserMeAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('me/', UserMeAPIView.as_view()),
]
