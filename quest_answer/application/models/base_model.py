from django.db import models

from application.constants import MAX_TEXT_LENGTH


class BaseModel(models.Model):
    '''Базовая модель для моделей вопросов и ответов.'''

    create_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH, verbose_name='Текст')

    class Meta:
        abstract = True
        ordering = ['-create_at']

    def __str__(self):
        return self.text
