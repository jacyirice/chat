from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from .models import Group
from django.views.generic import CreateView, FormView
from .forms import GroupForm, EnterGroupForm
# Create your views here.


@login_required
def index(request):
	groups = request.user.my_groups.all()
	return render(request, 'chat/room_list.html', {'groups': groups})


@login_required
def room(request, room_name):
	group = get_object_or_404(Group, pk=room_name, members__user=request.user)
	return render(request, 'chat/room_detail.html', {
		'group': group,
		'room_name': group.pk
	})


class GroupCreate(LoginRequiredMixin, FormView):
	template_name = 'chat/room_form.html'
	form_class = GroupForm
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		dados = form.clean()
		group = Group.objects.create(**dados)
		self.request.user.my_groups.create(group=group, office=1)
		return super().form_valid(form)


class GroupEnterView(LoginRequiredMixin, FormView):
	template_name = 'chat/enter_room_form.html'
	form_class = EnterGroupForm

	def form_valid(self, form):
		dados = form.clean()
		group = dados.get('group')
		if not group:
			form.add_error('group', 'Grupo inexistente.')
			return super().form_invalid(form)

		obj, created = group.members.get_or_create(user=self.request.user)
		if not created:
			form.add_error('group', 'Você já pertence a esse grupo.')
			return super().form_invalid(form)
		self.g = group.pk
		return super().form_valid(form)

	def get_success_url(self):
		room_name=self.g
		return reverse_lazy('room', kwargs={'room_name': room_name})