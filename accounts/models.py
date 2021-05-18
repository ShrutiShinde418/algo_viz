from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100, unique=True)
    password=models.CharField(max_length=75)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


    


# Create your models here.
