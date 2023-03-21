from django.forms import ModelForm


class TranslationForm(ModelForm):
    class Meta:
        #model = Translation
        fields = ['english', 'ipa']