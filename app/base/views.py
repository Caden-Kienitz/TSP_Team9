from django.shortcuts import render
from django.http import JsonResponse
from eng_to_ipa import convert

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import nameForm
import subprocess

def getName(request):
    if request.method == 'POST':
        form = nameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
            return HttpResponseRedirect('/')
    else:
        form = nameForm()
    return render(request, 'home.html', {'form': form})
    
def script(request):
    form = nameForm()
    if request.method == 'POST':
        info = request.POST['your phrase']
        output = convert(info)
        #output = subprocess.check_call(['python', '/script.py', info])
        # Here you are calling script_function,
        # passing the POST data for 'info' to it;
    #return render(request, 'home', {'output': output})
    return JsonResponse({'output': output})


def run_script(request):
    # get the english word from the request
    user_input = request.POST.get('your phrase')

    # convert the english word to ipa
    output = convert(user_input)  

    # return a JSON response
    return JsonResponse({'output': output})
from .forms import nameForm
import subprocess

def getName(request):
    if request.method == 'POST':
        form = nameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
            return HttpResponseRedirect('/')
    else:
        form = nameForm()
    return render(request, 'home.html', {'form': form})

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


