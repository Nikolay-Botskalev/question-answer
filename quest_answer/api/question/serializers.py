from rest_framework import serializers

from api.answer.serializers import AnswerCreateSerializer
from application.models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов."""

    class Meta:
        fields = ('id', 'text',)
        read_only_fields = ('id',)
        model = Question
        extra_kwargs = {
            'text': {'required': True, 'allow_blank': False}
        }


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов."""

    answer = AnswerCreateSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'text', 'answer',)
        model = Question
