from http import HTTPStatus

import pytest
from django.urls import reverse

from tests.constants import ANSWER_TEXT, USER_ID


pytestmark = pytest.mark.django_db


def test_create_answer(api_client, create_question):
    """Тест создания ответа на вопрос."""
    question = create_question()

    url = reverse('create-answer', kwargs={'id': question.id})
    data = {
        'question': question,
        'text': ANSWER_TEXT,
        'user_id': USER_ID,
    }
    response = api_client.post(url, data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.data['text'] == data['text']
    assert response.data['user_id'] == data['user_id']


def test_retrieve_answer(api_client, create_question, create_answer):
    """Тест получения одиночного ответа."""
    question = create_question()
    answer = create_answer(question=question)

    url = reverse('detail-answer', kwargs={'id': answer.id})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_retrieve_answer_with_undefined_index(api_client):
    """Тест получения одиночного ответа."""
    url = reverse('detail-answer', kwargs={'id': 100})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_answer(api_client, create_question, create_answer):
    """Тест удаления ответа."""
    question = create_question()
    answer = create_answer(question=question)

    url = reverse('detail-answer', kwargs={'id': answer.id})
    response = api_client.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
