from .models import Quiz, Question, CustomUser  
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import QuizSerializer, QuestionSerializer, userSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = userSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id']
	permission_classes = [IsAuthenticated]

class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer
	permission_classes = [IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = [IsAuthenticated]