from rest_framework import serializers
from .models import Quiz, Question, CustomUser
MULTIPLE_CHOICE = 1
BOOLEAN = 2
DROPDOWN = 3
NUMERICAL = 4
FREE_RESPONSE = 5

TYPE_CHOICES = [
    (MULTIPLE_CHOICE, 'multiple choice'),  
    (BOOLEAN, 'boolean'),
    (DROPDOWN, 'dropdown'),
    (NUMERICAL, 'numerical'),
    (FREE_RESPONSE, 'free response'),
]

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
            role=validated_data['role']
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
        valid_choices = [1,2,3,4,5]
        if not isinstance(value, list):
            raise serializers.ValidationError("Types must be a list.")
        if not set(value).issubset(set(valid_choices)):
            raise serializers.ValidationError("Invalid type choice.")
        results = []
        for item in value:
            results.append(TYPE_CHOICES[item-1][1])
        return results
        