from django import forms
from .models import Entry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['entry_title','entry']

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
