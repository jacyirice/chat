from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Group

# Create your views here.

@login_required
def index(request):
    groups = request.user.my_groups.all()
    return render(request, 'chat/index.html', {'groups':groups})

@login_required
def room(request, room_name):
    group = get_object_or_404(Group, pk=room_name)
    return render(request, 'chat/room.html', {
        'group': group,
        'room_name': group.pk
    })
