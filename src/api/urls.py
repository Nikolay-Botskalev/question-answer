from django.urls import path

from api.answer.views import AnswerCreateView, AnswerView
from api.question.views import QuestionDetailView, QuestionView

urlpatterns = [
    path('answers/<int:id>', AnswerView.as_view(), name='detail-answer'),
    path(
        'questions/<int:id>/answers/',
        AnswerCreateView.as_view(),
        name='create-answer'),
    path(
        'questions/<int:id>',
        QuestionDetailView.as_view(),
        name='detail-question'),
    path('questions/', QuestionView.as_view(), name='list-questions'),
]
