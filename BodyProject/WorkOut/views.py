from django.shortcuts import render , redirect
from django.shortcuts import render ,HttpResponse
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


def Create(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        Height = request.POST.get('Height', '')
        Weight = request.POST.get('Weight', '')
        age = request.POST.get('age', '')


        # basic validation
        if name and Height and Weight and age:
            Create = Body_info(
                name=name,
                Height=Height,
                Weight=Weight,
                age=age

            )
            Create.save()
            return HttpResponse("<h1>Thanks</h1>")
        else:
            return HttpResponse("<h1>Error: Please fill in all required fields</h1>")

    return render(request, 'players.html')

def update(request, player_id):
    # Retrieve the player instance
    player = get_object_or_404(Body_info, pk=player_id)

    if request.method == "POST":
        
        name = request.POST.get('name', '')
        height = request.POST.get('Height', '')
        weight = request.POST.get('Weight', '')
        age = request.POST.get('age', '')

        # Update the player instance with the new data
        player.name = name
        player.Height = height
        player.Weight = weight
        player.age = age

        # Save the updated player instance
        player.save()

        return HttpResponse("<h1>Player information updated successfully</h1>")
    return render(request, 'players.html')

def delete(request):
            body_info_instances = Body_info.objects.all()
            body_info_instances.delete()
            return HttpResponse("<h1>All data deleted successfully</h1>")



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
