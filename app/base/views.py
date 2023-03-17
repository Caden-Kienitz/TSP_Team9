from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def LogIn(request):
    return render(request, "LogIn.html")
def Contact(request):
    return render(request,"Contact.html")