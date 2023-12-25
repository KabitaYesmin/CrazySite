# forms.py
from django import forms
from .models import *


class imagesForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ['name', 'Main_Img']