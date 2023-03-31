from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login, name="login"),
    path("help/", views.help, name="help"),
    path("contact/", views.contact, name="contact"),
    path("Registration/", views.registration,name="registration")
    path('run-script/', views.run_script, name='run_script'),
    path('script/', views.script, name='script'),

]
