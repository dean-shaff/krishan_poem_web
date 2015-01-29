from poem_gen.models import TextInput
# from django.contrib.auth.models import User 
from django import forms
from django.utils import timezone

class PoemGenUploadForm(forms.Form):
    name = forms.CharField(help_text="Title")
    author = forms.CharField(help_text="Author")
    file = forms.FileField(help_text="Upload File")
    # password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
    class Meta:
        model = TextInput
        fields = ['name','author','file']