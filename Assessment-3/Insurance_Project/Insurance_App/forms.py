from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = '__all__'


class policies_form(forms.ModelForm):
    class Meta:
        model = user_policies_new
        fields = '__all__'

class grant_policy(forms.ModelForm):
    class Meta:
        model = user_policies_new
        fields = '__all__'

class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'


class update_form(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = ["password"]

class update_profile_f(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = ['firstname', 'lastname','username','password' ,'city', 'state','mobile']
