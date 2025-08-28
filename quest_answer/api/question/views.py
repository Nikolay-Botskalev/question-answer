from rest_framework import generics, viewsets 

from api.answer.serializers import AnswerSerializer
from api.question.serializers import QuestionSerializer
from application.models.question import Question


class AnswerCreateView(generics.CreateAPIView):
    """Класс для создания объекта ответа на вопрос."""

    serializer_class = AnswerSerializer
    lookup_field = 'id'


class QuestionViewSet(viewsets.ModelViewSet):
    """Класс для операций с объектами вопросов."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ('get', 'post', 'delete',)
