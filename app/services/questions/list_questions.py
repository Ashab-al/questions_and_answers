from models.question import Question
from sqlalchemy.ext.asyncio import AsyncSession
from query_objects.questions.get_all_questions import get_all_questions


async def list_questions(session: AsyncSession) -> list[Question]:
    """
    Возвращает список всех вопросов из базы данных.

    Args:
        session (AsyncSession): асинхронная сессия SQLAlchemy для операций с БД.

    Returns:
        list[Question]: список всех вопросов в базе данных.
    """
    questions: list[Question] = await get_all_questions(session)

    return questions
