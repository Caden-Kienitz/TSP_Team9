from django.shortcuts import render
from django.http import JsonResponse
from eng_to_ipa import convert

def run_script(request):
    # get the english word from the request
    user_input = request.POST.get('user_input')

    # convert the english word to ipa
    output = convert(user_input)  

    # return a JSON response
    return JsonResponse({'output': ipa})

def home(request):
    return render(request, "home.html")
def login(request):
    return render(request, "login.html")
def help(request):
    return render(request,"help.html")
def contact(request):
    return render(request,"contact.html")


