from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name="account"
urlpatterns = [
    url(r'login/$', views.user_login, name="user_login"),
    url(r'register/$', views.register, name="user_register"),
    url(r'logout/$', views.logout_then_login, name="user_logout"),
]