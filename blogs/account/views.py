from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome You. You have been authenticated sucessfully")
            else:
                return HttpResponse("Sorry, Your username or password is not correct.")
        else:
            return HttpResponse("Invalid Login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {'form': login_form})