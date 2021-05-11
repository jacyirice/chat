from django.shortcuts import render, redirect, get_object_or_404
from .models import Group

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        groups = request.user.my_groups.all()
        return render(request, 'chat/index.html', {'groups':groups})
    return redirect('/account/login')


def room(request, room_name):
    if request.user.is_authenticated:
        group = get_object_or_404(Group, pk=room_name)
        return render(request, 'chat/room.html', {
            'group': group,
            'room_name': group.pk
        })
    return redirect('/account/login')
