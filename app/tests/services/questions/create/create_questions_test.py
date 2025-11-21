from unittest.mock import AsyncMock
import pytest
from services.questions.create_question import create_questions
from schemas.questions.create.request import CreateQuestionRequest
from models.question import Question


@pytest.mark.asyncio
async def test_create_question():
    mock_db = AsyncMock()
    question_text = "Какой-то вопрос"
    question_data = CreateQuestionRequest(text=question_text)

    question: Question = await create_questions(
        session=mock_db, create_question=question_data
    )

    mock_db.commit.assert_awaited_once()
    mock_db.refresh.assert_awaited_once_with(question)
    assert question.text == question_text
    assert isinstance(question, Question)
