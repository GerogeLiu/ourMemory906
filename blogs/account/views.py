from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import LoginForm, RegistrationForm, UserProfileForm


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("blog:blog_title"))
            else:
                error_msg = "Sorry, Your username or password is not correct."
                login_form = LoginForm()
                return render(request, "account/login.html", {'error': error_msg, 'form':login_form})
        else:
            return HttpResponse("Invalid Login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {'form': login_form})



def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() * userprofile_form.is_valid():
            # user表
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # userprofile 表
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            return HttpResponseRedirect(reverse("account:user_login"))

        else:
            return HttpResponse("对不起，您没有注册成功")

    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {'form': user_form, 'profile': userprofile_form})


# 登出
def logout_then_login(request):
    logout(request)
    return HttpResponseRedirect(reverse("account:user_login"))