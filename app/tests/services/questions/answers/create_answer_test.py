import random
import uuid
from unittest.mock import AsyncMock, patch
import pytest
from models.question import Question
from models.answer import Answer
from services.questions.answers.create_answer import create_answer
from schemas.questions.answers.create.request import CreateAnswerRequest

@pytest.mark.asyncio
@patch("services.questions.answers.create_answer.get_question_by_id")
async def test_create_answer(mock_get_question_by_id):
    id_question = random.randint(1, 10)
    text = "Какой-то текст"
    uuid4 = str(uuid.uuid4())

    mock_db = AsyncMock()
    new_question = Question(id=id_question, text=text)
    text_answer = "Какой-то текст 123"
    create_answer_request = CreateAnswerRequest(text=text_answer, user_id=uuid4)
    mock_get_question_by_id.return_value = new_question

    new_answer = await create_answer(mock_db, id_question, create_answer_request)

    mock_get_question_by_id.assert_awaited_once()

    assert new_answer.text == text_answer
    assert new_answer.user_id == uuid4