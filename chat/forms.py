from django import forms
from .models import Group, GroupUser
class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['title','description','limit','image']
		widgets={
			'title':forms.TextInput(attrs={'class': 'form-control pb-1', 'placeholder':'Titulo do grupo'}),
			'description':forms.TextInput(attrs={'class': 'form-control pb-1', 'placeholder':'Descrição'}),
			'limit':forms.NumberInput(attrs={'class': 'form-control pb-1', 'placeholder':'Limite'}),
			'image':forms.FileInput(attrs={'class': 'form-control pb-1', 'placeholder':'Imagem do grupo'}),
		}

class EnterGroupForm(forms.ModelForm):
	class Meta:
		model = GroupUser
		fields = ['group']
		widgets={
			'group':forms.TextInput(attrs={'class': 'form-control pb-1', 'placeholder':'Codigo do grupo'}),
		}