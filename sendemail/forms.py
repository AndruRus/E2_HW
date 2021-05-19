from django import forms
from django.conf import settings
from django.core.mail import send_mail
import threading
from sendemail.models import EmailList


class ContactForm(forms.ModelForm):
    email = forms.EmailField(max_length=256, required=False)
    delay = forms.IntegerField(widget=forms.NumberInput)
    message = forms.CharField(widget=forms.Textarea)

    
    class Meta:  
        model = EmailList
        fields = '__all__'