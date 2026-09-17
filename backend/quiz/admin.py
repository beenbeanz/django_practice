from django.contrib import admin
from .models import CustomUser, Quiz, Question
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Quiz)
admin.site.register(Question)   