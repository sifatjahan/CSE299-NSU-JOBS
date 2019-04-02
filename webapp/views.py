from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Login


def user_login(request):
    context = {}
    next = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('webapp:home')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')

    else:
        return render(request, 'auth/login.html', context)

# Signup


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('webapp:home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

# Logout


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('webapp:login')


def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

# Show Student Profile


def student_profile(request, userID):
    user = User.objects.get(username=userID)

    return render(request, 'profile/student.html', {'user': user})

# Add/Edit Student Profile


def cv(request):

    user = request.user

    if request.method == 'POST':

        form = AddStudent(request.POST)

        if form.is_valid():
            profile = Student(
                user=user,
                std_email=form.cleaned_data['std_email'],
                std_name=form.cleaned_data['std_name'],
                std_bio=form.cleaned_data['std_bio'],
                std_contact=form.cleaned_data['std_contact'],
                ssc_int=form.cleaned_data['ssc_int'],
                ssc_year=form.cleaned_data['ssc_year'],
                ssc_cgpa=form.cleaned_data['ssc_cgpa'],
                hsc_int=form.cleaned_data['hsc_int'],
                hsc_year=form.cleaned_data['hsc_year'],
                hsc_cgpa=form.cleaned_data['hsc_cgpa'],
                honor_int=form.cleaned_data['honor_int'],
                honor_year=form.cleaned_data['honor_year'],
                honor_cgpa=form.cleaned_data['honor_cgpa'],
                master_int=form.cleaned_data['master_int'],
                master_year=form.cleaned_data['master_year'],
                master_cgpa=form.cleaned_data['master_cgpa'],
                skills=form.cleaned_data['skills'],
                experience=form.cleaned_data['experience'],
                awards=form.cleaned_data['awards'],
            )
            profile.save()
            messages.success(request, 'CV added/edited!')
            return redirect('webapp:profile')
        
        else:
            messages.warning(request, 'CV couldn\'t be added/edited!')
            return redirect('webapp:profile')

    else:
        form = AddStudent()
        return render(request, 'profile/cv.html', {'form': form, 'user': user})



# Show Company Profile


def company_profile(request, userID):
    user = User.objects.get(username=userID)

    return render(request, 'profile/company.html', {'user', user})

# Show Job request


def view_job(request, ID):
    return render(request, 'jobs/view.html', {})

# List Job request


def list_all_jobs(request):
    jobs = []
    return jobs


def show_jobs(request, list):
    return render(request, 'jobs/list.html', {})

# Add Job requests


def add_job(request):
    return render(request, 'jobs/add.html', {})

# Search Job requests


def search_job(request):
    jobs = []
    return jobs

# Search Student's Skill


def search_skill(request):
    pass
