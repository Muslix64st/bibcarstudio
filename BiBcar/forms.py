from django import forms
from .models import *
from django.forms import Textarea
from django.forms import TextInput

# import phonenumbers
# # from phonenumbers import *
#

class AddPostForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['name', 'phone_number', 'car_number', 'message']
        widget = {'message': TextInput(attrs={'cols': 80, 'rows': 20})}

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get("phone_number")
    #     z = phonenumbers.parse(phone_number, 'ru')
    #     if not phonenumbers.is_valid_number(z):
    #         raise forms.ValidationError("Number not in SG format")
    #     return phone_number
    #


