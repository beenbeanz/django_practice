# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Quiz, Question

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "role", "is_staff", "is_active")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("role", "is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ("question", "type", "answer", "incorrect")

class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "creator")
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "type", "quiz")
    list_filter = ("type", "quiz")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)