from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from search.models import CovidUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class CovidUserInfoForm(forms.Form):
    country = forms.CharField(max_length=30, required=True, help_text='')
    city = forms.CharField(max_length=30, required=True, help_text='')
    has_covid = forms.BooleanField(required=False,initial=True)
    has_data = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CovidUser
        fields = ('country', 'city', 'has_covid', "has_data")


