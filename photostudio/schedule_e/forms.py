from django import forms
from django.utils.translation import gettext_lazy as _


class EventForm(forms.Form):
    title = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    phonenumber = forms.CharField()
    email = forms.EmailField(max_length=200)
    hall = forms.CharField()
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    description = forms.CharField(max_length=200)
    #user = forms.ForeignKey(User, on_delete=forms.SET_NULL, null=True)



