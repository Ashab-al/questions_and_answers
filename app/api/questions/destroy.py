from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from services.questions.destroy_question import destroy_question
from schemas.questions.destroy.response import DestroyQuestionResponse
router = APIRouter()
@router.delete(
    "/{question_id}",
    summary="Удалить вопрос",
    description="Удаляет вопрос по его ID из базы данных.",
    response_model=DestroyQuestionResponse,
)
async def destroy(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    question_id: Annotated[int, Path()],
):
    """
    Эндпоинт для удаления вопроса по его уникальному идентификатору.

    Пытается удалить вопрос из базы данных. Если вопрос не найден, возвращает ошибку 404.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy, внедряемая через зависимость.
        question_id (int): Идентификатор вопроса, переданный в пути запроса.
            Должен быть целым положительным числом.

    Returns:
        Question: Объект удалённого вопроса в формате JSON.
            Содержит: id, text, created_at, updated_at.

    Raises:
        HTTPException: С кодом 404, если вопрос с указанным `question_id` не найден.
            Сообщение об ошибке берётся из выброшенного `ValueError`.
    """
    try:
        question = await destroy_question(session, question_id)
    except ValueError as e:
        raise HTTPException(404, detail=str(e)) from e

    return question