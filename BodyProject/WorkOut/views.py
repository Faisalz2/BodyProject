from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from .models import Body_info

def wlcpag(request):
    return render(request,'base.html')

def BodyList(request):
    Bodys = Body_info.objects.all()
    BodyList = []
    for User in Bodys:
        BodyList.append({'User':User})

    context = {'BodyList':BodyList}
    return render(request,'BodyList.html',context)

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
