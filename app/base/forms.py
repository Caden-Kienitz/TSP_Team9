from django.forms import ModelForm
from django import forms

class nameForm(forms.Form):
    your_name = forms.CharField(label="your phrase", max_length=100)
