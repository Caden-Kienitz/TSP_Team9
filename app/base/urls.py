from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login, name="login"),
    path("help/", views.help, name="help"),
    path("contact/", views.contact, name="contact"),
]