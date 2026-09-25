from .models import Quiz, Question, CustomUser, QuestionInstance
from .serializers import QuestionInstanceSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
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
			permission_classes = [IsAuthenticated]
		return [p() for p in permission_classes]
	#might not need all these funcs below
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data) 
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	
	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.submitted:
			return Response({"error": "Cannot delete a question instance for a submitted quiz."}, status=400)
		self.perform_destroy(instance)
		return Response(status=status.HTTP_204_NO_CONTENT)

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.submitted:
			return Response({"error": "Cannot update a question instance for a submitted quiz."}, status=400)
		return super().update(request, *args, **kwargs)
	
		
class QuestionInstanceViewSet(viewsets.ModelViewSet):
	queryset = QuestionInstance.objects.all()
	serializer_class = QuestionInstanceSerializer

	def get_permissions(self):
			if self.action in ['create', 'update', 'destroy']:
				permission_classes = [IsTeacher]
			else:
				permission_classes = [IsAuthenticated]
			return [p() for p in permission_classes]

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.submitted:
			return Response({"error": "Cannot update a question instance for a submitted quiz."}, status=400)
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		instance = serializer.save()
		return Response(QuestionInstanceSerializer(instance).data, status=status.HTTP_200_OK)

	
