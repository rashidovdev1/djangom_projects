from django.urls import path
from . import views

urlpatterns = [
    path('<int:lesson_id>/', views.quiz_view, name='quiz'),
]
