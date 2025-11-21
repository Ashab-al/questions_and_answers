from models.question import Question
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload


async def get_all_questions(db: AsyncSession):
    """
    Получить список всех вопросов с предзагруженными ответами.

    Args:
        db (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        list[Question]: Список всех вопросов с их ответами.
    """
    questions = (
        (await db.execute(select(Question).options(joinedload(Question.answers))))
        .unique()
        .scalars()
        .all()
    )

    return questions
