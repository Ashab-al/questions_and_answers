from models.question import Question
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload


async def get_question_by_id(
    db: AsyncSession,
    question_id: int
) -> Question | None:
    """Получить вопрос с предзагруженными ответами."""
    return (
        (
            await db.execute(
                select(Question)
                .where(Question.id == question_id)
                .options(joinedload(Question.answers))
            )
        )
        .unique()
        .scalars()
        .first()
    )
