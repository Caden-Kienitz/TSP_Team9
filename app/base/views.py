from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def login(request):
    return render(request, "login.html")
def help(request):
    return render(request,"help.html")
def contact(request):
    return render(request,"contact.html")