import random
import uuid
from unittest.mock import AsyncMock, patch
import pytest
from services.answers.destroy_answer_by_id import destroy_answer_by_id
from models.answer import Answer


@pytest.mark.asyncio
@patch("services.answers.destroy_answer_by_id.get_answer_by_id")
async def test_destroy_question(mock_get_answer_by_id):
    mock_db = AsyncMock()
    mock_db = AsyncMock()
    answer_id = random.randint(1, 10)
    uuid4 = str(uuid.uuid4())
    question_id = random.randint(1, 10)

    new_answer = Answer(id=answer_id, text="Какой-то текст", user_id=uuid4, question_id=question_id)
    mock_get_answer_by_id.return_value = new_answer

    answer: Answer = await destroy_answer_by_id(
        db=mock_db, answer_id=answer_id
    )

    assert answer.text == new_answer.text
    assert isinstance(answer, Answer)
