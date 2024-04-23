from django import forms

from .models import Calculation

class calculationForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['principal', 'rate', 'time']
        