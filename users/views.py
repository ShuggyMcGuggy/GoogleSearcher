from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def my_view(request):
    return render(request, 'users/login.html')
        # Return an 'invalid login' error message.


def my_view2(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'users/test_page.html')

    else:
        return render(request, 'users/test_page.html')
        # Return an 'invalid login' error message.

def logout_view(request):
    """log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process the completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to a home page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1']
                                              )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
