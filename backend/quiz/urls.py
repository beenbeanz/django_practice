from django.urls import include, path
from quiz.views import QuestionInstanceViewSet, UserViewSet, QuizViewSet, QuestionViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny

class OpenAPIRootRouter(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        view = super().get_api_root_view(api_urls)
        view.cls.permission_classes = [AllowAny]
        return view

router = OpenAPIRootRouter()
router.register("users", UserViewSet)
router.register("quizzes", QuizViewSet)
router.register("questions", QuestionViewSet)
router.register("questioninstance", QuestionInstanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]