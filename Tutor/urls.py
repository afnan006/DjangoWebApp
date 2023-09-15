from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('tutor_list/', views.tutor_list, name='tutor_list'),
    # Define other URL patterns for tutor views here
]
