from django.db import models
from django.contrib.auth.models import AbstractUser

# universidades = [
#     ('UNNE', 'unne.'),
#     ('UTN', 'utn'),
#     ('UNCAUS', 'uncaus'),
#    ]

class Usuario(AbstractUser):

    provincia = models.CharField(max_length=30, null=True)
    ciudad = models.CharField(max_length=30, null=True)
    # universidad = models.CharField(max_length=50,  choices=universidades)
    domicilio = models.CharField(max_length=50, null=True)
    # imagen_profile = models.ImageField(upload_to='userProfile', null = True,blank=True)
    pass

