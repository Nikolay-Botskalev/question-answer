from django.db import models

from application.models.base_model import BaseModel
from application.constants import MAX_QUESTION_LENGTH


class Question(BaseModel):
    '''Модель вопроса.'''

    text = models.CharField(
        max_length=MAX_QUESTION_LENGTH, verbose_name='Текст вопроса')
