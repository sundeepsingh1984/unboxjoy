from django import forms
from django.forms import  EmailInput
from .models import ContactRequest,NewsletterSubscribers


class ContactRequestForm(forms.ModelForm):

    class Meta:
        model = ContactRequest
        fields = "__all__"


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscribers
        fields = ("email_id",)
        widgets = {
            'email_id': EmailInput(attrs={'placeholder': 'Enter Your Email Id here',"class":"form-group"}),
        }




