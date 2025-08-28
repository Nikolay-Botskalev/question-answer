from rest_framework import serializers

from application.models.answer import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для ответов."""

    class Meta:
        fields = ('question', 'user_id', 'text')
        model = Answer
