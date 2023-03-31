from django.shortcuts import render
from django.http import JsonResponse
from eng_to_ipa import convert
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import nameForm

#takes the POST data from the form and passes it to the convert function   
def home(request):
    form = nameForm()
    if request.method == 'POST':   
        info = request.POST['your phrase']
        # passing the POST data for 'info' to the convert function;
        output = convert(info)
        # returning the output as a JSON object
        return JsonResponse({'output': output}) 
    # if the request is not a POST, then return the home page
    return render(request, 'home.html', {'form': form})

def getName(request):
    if request.method == 'POST':
        form = nameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
            return HttpResponseRedirect('/')
    else:
        form = nameForm()
    return render(request, 'home.html', {'form': form})

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")
def help(request):
    return render(request,"help.html")
def contact(request):
    return render(request,"contact.html")
def registration(request):
    return render(request,"registration.html")


