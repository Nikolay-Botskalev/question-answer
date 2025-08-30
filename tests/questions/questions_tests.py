from http import HTTPStatus

import pytest
from django.urls import reverse

from tests.constants import COUNT_QUESTION, QUESTION_TEXT


pytestmark = pytest.mark.django_db


def test_list_questions(api_client, create_question):
    """Тест получения списка вопросов."""

    for i in range(COUNT_QUESTION):
        create_question(text=f"Вопрос {i+1}")

    url = reverse('list-questions')
    response = api_client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == COUNT_QUESTION


def test_create_question(api_client):
    """Тест создания вопроса."""

    url = reverse('list-questions')
    data = {'text': QUESTION_TEXT}
    response = api_client.post(url, data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.data['text'] == data['text']


def test_retrieve_question(api_client, create_question):
    """Тест получения одиночного вопроса."""
    question = create_question()

    url = reverse('detail-question', kwargs={'id': question.id})
    response = api_client.get(url)

    assert response.status_code == HTTPStatus.OK


def test_retrieve_with_undefined_index(api_client):
    """Тест получения несуществующего вопроса."""
    url = reverse('detail-question', kwargs={'id': 100})
    response = api_client.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_question(api_client, create_question):
    """Тест удаления вопроса."""
    question = create_question()

    url = reverse('detail-question', kwargs={'id': question.id})
    response = api_client.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
