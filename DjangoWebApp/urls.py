from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),  # Replace 'login_view' with your actual login view function

    # Include the URLs from each app
    path('student/', include('student.urls')),
    path('tutor/', include('tutor.urls')),
    path('admin/', include('admin.urls')),
    # Add other URL patterns as needed
]
