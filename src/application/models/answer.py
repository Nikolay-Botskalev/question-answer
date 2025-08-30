from django.db import models

from application.models.base_model import BaseModel


class Answer(BaseModel):
    """Модель ответа."""

    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, related_name='answer')
    user_id = models.UUIDField(verbose_name='Пользователь')
