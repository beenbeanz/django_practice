from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    USER = 1
    SUPERVISOR = 2
    ROLE_CHOICES = ((USER, 'user'), (SUPERVISOR, 'supervisor'))
    role = models.CharField(choices=ROLE_CHOICES, null=False, default=(USER, 'user'))

    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)          

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = BaseUserManager()

    def __str__(self):
    	return "{}".format(self.email)

class Quiz(models.Model):
    types = models.JSONField()
    title = models.CharField(max_length=255, null=False)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        CustomUser, null=False, 
        on_delete=models.CASCADE
        )
    def __str__(self):
        return str(self.id)

class Question(models.Model):
    question = models.CharField(max_length=255, null=False)
    answer = models.JSONField(default=list)
    incorrect = models.JSONField(default=list, blank=True, null=True)
    quiz = models.ForeignKey(Quiz, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    