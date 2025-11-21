from models.answer import Answer
from sqlalchemy.ext.asyncio import AsyncSession
from query_objects.answers.get_answer_by_id import get_answer_by_id

async def find_answer_by_id(
    db: AsyncSession,
    answer_id: int
) -> Answer:

    answer: Answer | None = await get_answer_by_id(db, answer_id)

    if not answer:
        raise ValueError(f"Answer с id - {answer_id} нет в базе данных")

    return answer
