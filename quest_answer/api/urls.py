from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.answer.views import AnswerViewSet
from api.question.views import QuestionViewSet, AnswerCreateView


app_name = 'api'

router = DefaultRouter()

router.register('questions', QuestionViewSet, basename='questions')
router.register('answers', AnswerViewSet, basename='answers')


urlpatterns = [
    path('questions/<int:id>/answers', AnswerCreateView.as_view()),
    path('', include(router.urls)),
]
