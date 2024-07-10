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
            'message': forms.Textarea(
                attrs={'placeholder': 'Your message (max 3000 characters)'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['mode_of_contact'].choices = [('', 'Contact by')] + list(
                self.fields['mode_of_contact'].choices)

        self.fields['question_categories'].choices = [(
            '', 'How can we help you?')] + list(self.fields[
                'question_categories'].choices)
