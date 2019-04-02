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


def student_profile(request):
    user = request.user

    return render(request, 'profile/student.html', {'user': user})

# Add/Edit Student Profile


def cv(request):

    user = request.user

    if request.method == 'POST':

        form = AddStudent(request.POST)

        if form.is_valid():
            user.student.std_email = form.cleaned_data['std_email'],
            user.student.std_name = form.cleaned_data['std_name'],
            user.student.std_bio = form.cleaned_data['std_bio'],
            user.student.std_contact = form.cleaned_data['std_contact'],
            user.student.ssc_int = form.cleaned_data['ssc_int'],
            user.student.ssc_year = form.cleaned_data['ssc_year'],
            user.student.ssc_cgpa = form.cleaned_data['ssc_cgpa'],
            user.student.hsc_int = form.cleaned_data['hsc_int'],
            user.student.hsc_year = form.cleaned_data['hsc_year'],
            user.student.hsc_cgpa = form.cleaned_data['hsc_cgpa'],
            user.student.honor_int = form.cleaned_data['honor_int'],
            user.student.honor_year = form.cleaned_data['honor_year'],
            user.student.honor_cgpa = form.cleaned_data['honor_cgpa'],
            user.student.master_int = form.cleaned_data['master_int'],
            user.student.master_year = form.cleaned_data['master_year'],
            user.student.master_cgpa = form.cleaned_data['master_cgpa'],
            user.student.skills = form.cleaned_data['skills'],
            user.student.experience = form.cleaned_data['experience'],
            user.student.awards = form.cleaned_data['awards'],
            user.save()
            messages.success(request, 'CV added/edited!')
            return redirect('webapp:profile')

        else:
            messages.warning(request, 'CV couldn\'t be added/edited!')
            return redirect('webapp:profile')

    else:
        form = AddStudent()
        return render(request, 'profile/cv.html', {'form': form, 'user': user})


# Show Company Profile


# def company_profile(request, userID):
#     user = User.objects.get(username=userID)

#     return render(request, 'profile/company.html', {'user', user})

# Add Job

def add_job(request):

    if request.method == 'POST':
        form = AddJobs(request.POST)

        if form.is_valid():
            job = Jobs(
                com_name = form.cleaned_data['com_name'],
                category = form.cleaned_data['category'],
                post = form.cleaned_data['post'],
                vacancy = form.cleaned_data['vacancy'],
                hours = form.cleaned_data['hours'],
                salary = form.cleaned_data['salary'],
                com_email = form.cleaned_data['com_email'],
                com_contact = form.cleaned_data['com_contact'],
            )
            job.save()
            messages.success(request, 'Job added!')
            return redirect('webapp:show_jobs')

        else:
            messages.warning(request, 'Job can\'t be added!')
            return redirect('webapp:show_jobs')

    else:
        form = AddJobs()
        return render(request, 'jobs/add.html', {'form': form})

# Show Job request

def view_job(request, ID):
    job = Jobs.objects.get(id=ID)
    return render(request, 'jobs/job.html', {'job': job})

# List Job request


# def list_all_jobs(request):
#     jobs = []
#     return jobs


def show_jobs(request):

    jobs = Jobs.objects.all()

    return render(request, 'jobs/list.html', {'jobs': jobs})

# Search Job requests


def search_job(request):
    jobs = []
    return jobs

# Search Student's Skill


def search_skill(request):
    pass
