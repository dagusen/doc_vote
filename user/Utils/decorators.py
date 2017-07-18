from functools import wraps
from django.conf import settings
import requests
import json


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
