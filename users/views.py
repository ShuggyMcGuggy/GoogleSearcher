from django.shortcuts import render
from django.contrib.auth import authenticate, login

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