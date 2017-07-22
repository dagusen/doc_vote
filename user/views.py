from django.contrib.auth import authenticate, login, logout
from .Utils.decorators import logged_in_user
from django.shortcuts import render, redirect
from .Forms import Login, Registration
from .Utils.decorators import add_recaptcha
from django.contrib import messages


@add_recaptcha
@logged_in_user(redirect_name="polls:index")
def user_login(request):
    if request.method == "GET":
        form = Login(None)
        return render(request, "user/login.html", {"form": form})

    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            if not request.recaptcha_valid:
                return render(request, "user/login.html", {"form": form, "error_message": "Please Fill Captcha"})

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Successfully Login")
                    return redirect("polls:index")
                else:
                    return render(request, "user/login.html",
                                  {"form": form, "error_message": "Sorry This user no longer active"})
            else:
                return render(request, "user/login.html", {"form": form, "error_message": "Sorry Wrong Credential"})

        return render(request, "user/login.html", {"form": form})


@add_recaptcha
@logged_in_user(redirect_name="polls:index")
def user_registration(request):
    if request.method == "GET":
        form = Registration(None)
        return render(request, "user/registration.html", {"form": form})

    if request.method == "POST":
        form = Registration(request.POST)

        if form.is_valid():
            if not request.recaptcha_valid:
                return render(request, "user/login.html", {"form": form, "error_message": "Please Fill Captcha"})

            user = form.save(commit=False)
            # Clean Data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Successfully register & login automatically")
                    return redirect("polls:index")
                else:
                    return render(request, "user/registration.html",
                                  {"form": form, "error_message": "Sorry this user is no longer active"})
        return render(request, "user/registration.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("user:user_login")
