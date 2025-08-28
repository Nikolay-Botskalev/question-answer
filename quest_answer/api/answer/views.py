from rest_framework import viewsets 

from api.answer.serializers import AnswerSerializer
from application.models.answer import Answer


class AnswerViewSet(viewsets.ModelViewSet):
    """Класс для CRUD операций с объектами вопросов."""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    http_method_names = ('get', 'post',)
