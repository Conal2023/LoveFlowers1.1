from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'mode_of_contact': forms.Select(attrs={'placeholder': 'Contact by'}),
            'question_categories': forms.Select(attrs={'placeholder': 'How can we help you?'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message (max 3000 characters)'}),
        }
