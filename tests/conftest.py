import pytest

from tests.constants import ANSWER_TEXT, QUESTION_TEXT, USER_ID


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def create_question():
    """Фикстура для создания вопросов."""
    from application.models.question import Question  # type: ignore

    def make_question(text=QUESTION_TEXT, **kwargs):
        return Question.objects.create(text=text, **kwargs)
    return make_question


@pytest.fixture
def create_answer():
    """Фикстура для создания ответов."""
    from application.models.answer import Answer  # type: ignore

    def make_answer(
        question,
        text=ANSWER_TEXT,
        user_id=USER_ID,
        **kwargs
    ):
        return Answer.objects.create(
            question=question,
            text=text,
            user_id=user_id,
            **kwargs
        )
    return make_answer


@pytest.fixture
def sample_question(create_question):
    """Фикстура для создания одного вопроса."""
    return create_question()


@pytest.fixture
def sample_answer(create_answer, sample_question):
    """Фикстура для создания одного ответа."""
    return create_answer(question=sample_question)
