from models.answer import Answer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_answer_by_id(
    db: AsyncSession,
    answer_id: int
) -> Answer | None:
    """Получить Answer."""
    return (
        (
            await db.execute(
                select(Answer)
                .where(Answer.id == answer_id)
            )
        )
        .scalars()
        .first()
    )
