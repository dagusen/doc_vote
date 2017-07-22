from functools import wraps

import requests
from django.conf import settings
from django.shortcuts import redirect


def add_recaptcha(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        request.recaptcha_valid = None
        if request.method == "POST":
            response = request.POST.get("g-recaptcha-response")
            url = "https://www.google.com/recaptcha/api/siteverify"
            data = {
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": response
            }
            push = requests.post(url, data=data)
            result = push.json()

            if result['success']:
                request.recaptcha_valid = True
            else:
                request.recaptcha_valid = False
        return func(request, *args, **kwargs)

    return wrapper


def logged_in_user(redirect_name=None, *margs, **mkwargs):
    def main_wrapper(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                print(redirect_name)
                return redirect(redirect_name, *margs, **mkwargs)
            func(request, *args, **kwargs)

        return wrapper

    return main_wrapper
