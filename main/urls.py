# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('status/', views.status, name='status'),
	path('login/', views.login_user, name='login'),
]