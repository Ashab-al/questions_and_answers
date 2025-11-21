from schemas.questions.create.request import CreateQuestionRequest
from sqlalchemy.ext.asyncio import AsyncSession
from models.question import Question

async def create_question(
    session: AsyncSession,
    new_question: CreateQuestionRequest,
):
    """
    Создаёт и сохраняет вопрос в базе данных.

    Args:
        session (AsyncSession): асинхронная сессия SQLAlchemy для операций с БД.
        new_question (CreateQuestionRequest): объект запроса с полем `text`.

    Returns:
        Question: созданный и обновлённый экземпляр модели Question.
    """
    question: Question = Question(text=new_question.text)

    session.add(question)

    await session.commit()
    await session.refresh(question)

    return question
