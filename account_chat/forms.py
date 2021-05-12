from django import forms
from django.contrib.auth import get_user_model
from chat.models import Group, GroupUser

User = get_user_model()

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email','first_name','last_name']
		widgets={
			'email':forms.EmailInput(attrs={'class': 'form-control pb-1', 'placeholder':'Email'}),
			'first_name':forms.TextInput(attrs={'class': 'form-control pb-1', 'placeholder':'Primeiro nome'}),
			'last_name':forms.TextInput(attrs={'class': 'form-control pb-1', 'placeholder':'Ultimo nome'}),
		}