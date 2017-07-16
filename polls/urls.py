from django.conf.urls import url
from .views import index, detail

urlpatterns = [
    # /polls
    url(r'^$', index, name="index"),

    # /polls/poll_id
    url(r'^(?P<poll_id>[0-9]+)$', detail, name="detail"),
]
