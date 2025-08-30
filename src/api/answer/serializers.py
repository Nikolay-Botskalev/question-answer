from rest_framework import serializers

from application.models.answer import Answer


class AnswerDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода одиночного ответа."""

    class Meta:
        fields = ('id', 'question_id', 'user_id', 'text')
        model = Answer


class AnswerCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания объекта ответа."""

    class Meta:
        fields = ('id', 'user_id', 'text')
        read_only_fields = ('id',)
        model = Answer
        extra_kwargs = {
            'text': {'required': True, 'allow_blank': False},
            'user_id': {'required': True},
        }
