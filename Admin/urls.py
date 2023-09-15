from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Use auth_views for the login view
    path('student/', include('student.urls')),
    path('tutor/', include('tutor.urls')),
    path('admin/', include('admin.urls')),
    # Add other URL patterns as needed
]
