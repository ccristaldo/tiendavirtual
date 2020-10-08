from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
	path('registro/', views.RegistroUsuario.as_view(), name='registro'),
]