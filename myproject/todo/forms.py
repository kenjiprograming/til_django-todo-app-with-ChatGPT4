from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'completed',
        ]
        widgets = {
            'title':        forms.TextInput(attrs={'class': 'form-input'}),
            'completed':    forms.CheckboxInput(attrs={'class': 'form-input'}),
        }