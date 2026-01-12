from django.urls import path
from .views import LabelListCreateAPIView , LabelDetailAPIView , TaskLabelAPIView

urlpatterns = [
    path('', LabelListCreateAPIView.as_view()),
    path('<int:pk>/', LabelDetailAPIView.as_view()),
    path('tasks/<int:task_id>/labels/<int:label_id>/', TaskLabelAPIView.as_view()),
]
