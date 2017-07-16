from django.conf.urls import url
from .views import index, detail, vote, result

urlpatterns = [
    # /polls
    url(r'^$', index, name="index"),

    # /polls/poll_id
    url(r'^(?P<poll_id>[0-9]+)$', detail, name="detail"),

    # /polls/poll_id
    url(r'^(?P<poll_id>[0-9]+)/vote$', vote, name="vote"),

    # /polls/poll_id/result
    url(r'^(?P<poll_id>[0-9]+)/result$', result, name="result"),
]
