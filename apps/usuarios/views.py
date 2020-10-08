from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegistroUsuarioForm
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

# Create your views here.
class RegistroUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioForm
	template_name = 'usuarios/registro.html'
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		'''
		En este parte, si el formulario es valido guardamos lo que se obtiene de él y 
		usamos authenticate para que el usuario incie sesión luego de haberse registrado 
		y lo redirigimos al index
		'''

		form.save()
		usuario = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		usuario = authenticate(username=usuario, password=password)
		login(self.request, usuario)
		return redirect('/')