from models.question import Question
from query_objects.questions.get_question_by_id import get_question_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.show.request import ShowQuestionRequest

async def find_question_by_id(
    db: AsyncSession,
    question_id: ShowQuestionRequest
) -> Question:

    question: Question | None = await get_question_by_id(db, question_id.id)

    if not question:
        raise ValueError(f"Вопроса с id - {question_id.id} нет в базе данных")

    return question
