from schemas.questions.create.request import CreateQuestionRequest
from sqlalchemy.ext.asyncio import AsyncSession
from models.question import Question
from models.answer import Answer
from query_objects.questions.get_question_by_id import get_question_by_id
from schemas.questions.answers.create.request import CreateAnswerRequest

async def create_answer(
    db: AsyncSession,
    question_id: int,
    answer_data: CreateAnswerRequest
):
    """
    Создаёт и сохраняет вопрос в базе данных.

    Args:
        session (AsyncSession): асинхронная сессия SQLAlchemy для операций с БД.
        new_question (CreateQuestionRequest): объект запроса с полем `text`.

    Returns:
        Question: созданный и обновлённый экземпляр модели Question.
    """
    question: Question | None = await get_question_by_id(db, question_id)

    if not question:
        raise ValueError(f"Вопроса с id - {question_id} нет в базе данных")

    answer = Answer(user_id=answer_data.user_id, text=answer_data.text)
    answer.question = question

    db.add(answer)

    await db.commit()
    await db.refresh(answer)

    return answer
