from django import forms
from .models import Breed

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите тему'
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
    )

    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Введите сообщение'
        })
    )

class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name', 'description', 'average_weight', 'life_expectancy', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'average_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'life_expectancy': forms.NumberInput(attrs={'class': 'form-control'}),
        }