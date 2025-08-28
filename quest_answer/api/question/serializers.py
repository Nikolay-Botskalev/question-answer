from rest_framework import serializers

from application.models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов."""

    class Meta:
        fields = ('text',)
        model = Question
