from django.contrib import admin
from .models import CustomUser, Quiz, Question
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Quiz)
admin.site.register(Question)   