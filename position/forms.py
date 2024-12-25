from django import forms
from .models import Position

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'order_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'order_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }