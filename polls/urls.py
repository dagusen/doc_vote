from django.conf.urls import url
from .views import index

urlpatterns = [
    # /polls
    url(r'^$', index, name="index"),
]
