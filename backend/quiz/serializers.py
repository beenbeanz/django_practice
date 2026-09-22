from rest_framework import serializers
from .models import Quiz, Question, CustomUser


TYPE_CHOICES = Question.Type.choices

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'password']
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', CustomUser.Role.USER)
        )
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'incorrect', 'quiz']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'types', 'title', 'creator']

    def validate_types(self, value):
        valid_choices = [choice[0] for choice in TYPE_CHOICES]
        if not isinstance(value, list):
            raise serializers.ValidationError("Types must be a list.")
        if not set(value).issubset(set(valid_choices)):
            raise serializers.ValidationError("Invalid type choice.")
        return value