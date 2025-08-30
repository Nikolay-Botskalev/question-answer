from django.shortcuts import get_object_or_404
from rest_framework import generics

from api.answer.serializers import (
    AnswerCreateSerializer,
    AnswerDetailSerializer,
)
from application.models.answer import Answer
from application.models.question import Question


class AnswerView(generics.RetrieveDestroyAPIView):
    """Класс для просмотра и удаления объекта ответа."""

    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer
    lookup_field = 'id'


class AnswerCreateView(generics.CreateAPIView):
    """Класс для создания объекта ответа на вопрос."""

    serializer_class = AnswerCreateSerializer

    def perform_create(self, serializer) -> None:
        """Метод устанавливает поле question для объекта ответа."""
        question_id = self.kwargs['id']
        question = get_object_or_404(Question, id=question_id)
        serializer.save(question=question)
