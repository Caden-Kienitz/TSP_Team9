from django.urls import path
from django.urls import include, re_path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path("", views.home, name="home"),
    # path("login/",views.login, name="login"),
    path("help/", views.help, name="help"),
    path("contact/", views.contact, name="contact"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]

    

