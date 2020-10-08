from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
	
	class Meta:
		model = Usuario
		fields = ['username',
				'first_name',
				'last_name',
				'domicilio',				
				'password1',
				'password2',
				'email',
				'provincia',
				'ciudad',
				]
		help_texts = {
				'username': None,
				'password1': None,
				'password2': None,
			}