from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ----------- HOME PAGE -----------
def home(request):
	player = []
	if request.user.is_authenticated:
		player = get_object_or_404(Player, pk=request.user.pk)
	return render(request, 'home.html', {'player': player})


# ----------- STATUS PAGE -----------
@login_required(login_url='login')
def status(request):
	player = get_object_or_404(Player, pk=request.user.pk)
	return render(request, 'status.html', {'player': player})


# ----------- LOGIN PAGE -----------
def login_user(request):
	return render(request, 'login.html', {})