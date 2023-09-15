# Import necessary modules
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Tutor

def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutor/tutor_list.html', {'tutors': tutors})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
