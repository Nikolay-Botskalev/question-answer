from rest_framework import generics

from api.question.serializers import (
    QuestionDetailSerializer,
    QuestionSerializer,
)
from application.models.question import Question


class QuestionView(generics.ListCreateAPIView):
    """Класс для создания вопроса и вывода списка вопросов."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailView(generics.RetrieveDestroyAPIView):
    """Класс для отображения и удаления записи."""

    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    lookup_field = 'id'
