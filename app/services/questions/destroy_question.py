from query_objects.questions.get_question_by_id import get_question_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from models.question import Question


async def destroy_question(
    db: AsyncSession,
    question_id: int
) -> Question:
    """
    Удаляет вопрос из базы данных по его идентификатору.

    Args:
        db (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.
        question_id (int): Уникальный идентификатор вопроса, который необходимо удалить.

    Returns:
        Question: Объект удалённого вопроса. Может использоваться для логирования или уведомлений.

    Raises:
        ValueError: Если вопрос с указанным `question_id` не найден в базе данных.
    """
    question = await get_question_by_id(db, question_id)

    if not question:
        raise ValueError(f"Вопроса с id - {question_id} нет в базе данных")

    await db.delete(question)
    await db.commit()

    return question
