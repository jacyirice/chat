from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

User = get_user_model()

# Create your views here.
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['email','first_name','last_name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

    def get_object(self, *args, **kwargs):
        return self.request.user