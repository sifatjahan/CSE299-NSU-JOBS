from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
    return render(request, 'home.html', {})

# Show Student Profile

# Add Student Profile

