import random
from unittest.mock import AsyncMock, patch
import pytest
from services.questions.destroy_question import destroy_question
from models.question import Question


@pytest.mark.asyncio
@patch("services.questions.destroy_question.get_question_by_id")
async def test_destroy_question(mock_get_question_by_id):
    mock_db = AsyncMock()
    question_text = "Какой-то вопрос"
    question_id = random.randint(1, 10)
    question_data = Question(id=question_id,text=question_text)
    mock_get_question_by_id.return_value = question_data

    question: Question = await destroy_question(
        db=mock_db, question_id=question_id
    )

    assert question.text == question_text
    assert isinstance(question, Question)
