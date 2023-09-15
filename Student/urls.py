from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    # Define other URL patterns for student views here
]
