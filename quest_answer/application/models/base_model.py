from django.db import models

from application.constants import DISPLAYED_LENGTH


class BaseModel(models.Model):
    '''Базовая модель для моделей вопросов и ответов.'''

    #text = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    """
    def __repr__(self):
        if len(self.text) > DISPLAYED_LENGTH:
            return self.text[:DISPLAYED_LENGTH] + '...'
        return self.text
    """

    class Meta:
        abstract = True
        ordering = ['-create_at']
