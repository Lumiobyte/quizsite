from django import forms
from .models import *

class createQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz