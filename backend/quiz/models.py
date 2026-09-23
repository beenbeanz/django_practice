from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", CustomUser.Role.SUPERVISOR)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    class Role(models.IntegerChoices):
        USER = 1, "User"
        SUPERVISOR = 2, "Supervisor"

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(
        choices=Role.choices,
        default=Role.USER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Quiz(models.Model):
    types = models.JSONField()
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quizzes",
    )

    def __str__(self):
        return self.title

class Question(models.Model):
    class Type(models.IntegerChoices):
        MULTIPLE_CHOICE = 1, "Multiple choice"
        BOOLEAN = 2, "Boolean"
        DROPDOWN = 3, "Dropdown"
        NUMERICAL = 4, "Numerical"

    question = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(choices=Type.choices, default=Type.MULTIPLE_CHOICE)
    answer = models.JSONField(default=list)
    incorrect = models.JSONField(default=list, blank=True)
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    def __str__(self):
        return str(self.id)

class QuestionInstance(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="instances",
    )
    type = models.PositiveSmallIntegerField(choices=Question.Type.choices, default=Question.Type.MULTIPLE_CHOICE)
    answer = models.JSONField(default=list)
    incorrect = models.JSONField(default=list, blank=True)
    