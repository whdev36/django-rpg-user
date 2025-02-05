from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ----------- HOME PAGE -----------
def home(request):
	player = []
	if request.user.is_authenticated:
		player = get_object_or_404(Player, pk=request.user.pk)
		# player.add_artifact('Shadow Sword', 50, 'A powerful dark blade.')
		# player.add_artifact("Dragon Blade", 50, "A legendary sword with dragon fire")
		# player.add_artifact("Shadow Cloak", 20, "Makes the wearer almost invisible in darkness")
		# player.add_artifact("Titan's Gauntlet", 40, "Gives superhuman strength")

	return render(request, 'home.html', {'player': player})


# ----------- STATUS PAGE -----------
@login_required(login_url='login')
def status(request):
	player = get_object_or_404(Player, pk=request.user.pk)
	return render(request, 'status.html', {'player': player})


# ----------- LOGIN PAGE -----------
def login_user(request):
	return render(request, 'login.html', {})