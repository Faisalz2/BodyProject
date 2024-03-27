from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from .models import Body_info

def wlcpag(request):
    return render(request,'base.html')


def calculate_calories_view(request):
    # Retrieve all Body_info instances from the database
    body_info_instances = Body_info.objects.all()

    # Calculate calories for each instance
    for body_info_instance in body_info_instances:
        body_info_instance.calories_needed = body_info_instance.calculate_calories()

    # Pass the instances to the template for rendering
    context = {
        'body_info_instances': body_info_instances
    }

    return render(request, 'BodyList.html', context)



def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('wlc')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
