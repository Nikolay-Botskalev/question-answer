from django.db import models

from application.models.base_model import BaseModel
from application.constants import MAX_ANSWER_LENGTH


class Answer(BaseModel):
    '''Модель ответа.'''

    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, related_name='answer')
    user_id = models.UUIDField(verbose_name='Пользователь')
    text = models.CharField(
        max_length=MAX_ANSWER_LENGTH, verbose_name='Текст ответа')
