from django import forms
from app.models import *

class TrainerForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields='__all__'
        