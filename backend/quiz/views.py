from .models import Quiz, Question, CustomUser  
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import QuizSerializer, QuestionSerializer, userSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = userSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id']

class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer