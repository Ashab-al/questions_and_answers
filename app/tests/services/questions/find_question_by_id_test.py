import random
from models.question import Question
from unittest.mock import AsyncMock, patch
import pytest
from services.questions.find_question_by_id import find_question_by_id


@pytest.mark.asyncio
@patch("services.questions.find_question_by_id.get_question_by_id")
async def test_find_question_by_id(mock_get_question_by_id):
    mock_db = AsyncMock()
    question_id = random.randint(1, 10)
    new_question = Question(id=question_id, text="Какой-то текст")

    mock_get_question_by_id.return_value = new_question

    question = await find_question_by_id(mock_db, new_question)

    mock_get_question_by_id.assert_awaited_once_with(mock_db, new_question.id)
    assert question.id == question_id
    assert question.text == new_question.text
