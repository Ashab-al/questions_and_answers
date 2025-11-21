from unittest.mock import AsyncMock, patch
import pytest
from services.questions.list_questions import list_questions
from models.question import Question


@pytest.mark.asyncio
@patch("services.questions.list_questions.get_all_questions")
async def test_list_questions(mock_get_all_questions):
    mock_db = AsyncMock()

    question1 = Question(id=1, text="Вопрос 1")
    question2 = Question(id=2, text="Вопрос 2")
    mock_get_all_questions.return_value = [question1, question2]

    questions_list = await list_questions(session=mock_db)

    mock_get_all_questions.assert_awaited_once()
    assert len(questions_list) == 2
    assert questions_list[0].text == question1.text
    assert questions_list[1].text == question2.text
