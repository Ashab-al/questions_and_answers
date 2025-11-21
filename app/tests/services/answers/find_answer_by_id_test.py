import random
import uuid
from models.answer import Answer
from unittest.mock import AsyncMock, patch
import pytest
from services.answers.find_answer_by_id import find_answer_by_id



@pytest.mark.asyncio
@patch("services.answers.find_answer_by_id.get_answer_by_id")
async def test_find_answer_by_id(mock_get_question_by_id):
    mock_db = AsyncMock()
    answer_id = random.randint(1, 10)
    uuid4 = str(uuid.uuid4())
    question_id = random.randint(1, 10)
    new_answer = Answer(id=answer_id, text="Какой-то текст", user_id=uuid4, question_id=question_id)

    mock_get_question_by_id.return_value = new_answer

    answer = await find_answer_by_id(mock_db, answer_id)

    mock_get_question_by_id.assert_awaited_once_with(mock_db, new_answer.id)
    assert answer.id == answer_id
    assert answer.text == new_answer.text
    assert answer.user_id == new_answer.user_id
