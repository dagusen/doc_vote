from django.conf.urls import url
from .views import user_login, user_registration, user_logout

urlpatterns = [
    url(r'^login$', user_login, name="user_login"),
    url(r'^signup', user_registration, name="user_signup"),
    url(r'^logout$', user_logout, name="user_logout"),
]
