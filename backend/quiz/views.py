from .models import Quiz, Question, CustomUser, QuestionInstance
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import QuizSerializer, QuestionSerializer, userSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacher, IsStudent

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

	def get_permissions(self):
		if self.action in ['create', 'update', 'destroy']:
			permission_classes = [IsTeacher]
		else:
			permission_classes = [IsAuthenticated]
		return [p() for p in permission_classes]

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = [IsAuthenticated]

	def get_permissions(self):
		if self.action in ['create', 'update', 'destroy']:
			permission_classes = [IsTeacher]
		else:
			permission_classes = []
		return [p() for p in permission_classes]
	
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data) 
		serializer.is_valid(raise_exception=True)
		serializer.save
	#def destroy(self, request, *args, **kwargs):

	#def update(self, request, *args, **kwargs):
	
		
class QuestionInstance(viewsets.ModelViewSet):
	queryset = QuestionInstance.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = [IsAuthenticated]

	def get_permissions(self):
			if self.action in ['create', 'update', 'destroy']:
				permission_classes = [IsTeacher]
			else:
				permission_classes = []
			return [p() for p in permission_classes]

	
