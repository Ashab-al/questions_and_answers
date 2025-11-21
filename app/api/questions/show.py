from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.show.request import ShowQuestionRequest
from schemas.questions.show.response import ShowQuestionResponse
from services.questions.find_question_by_id import find_question_by_id

router = APIRouter()
@router.get(
    "/{id}",
    summary="Получить вопрос и все ответы на него",
    description="Возвращает вопрос по его ID вместе со всеми связанными ответами.",
    response_model=ShowQuestionResponse,
)
async def show_question(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    question_id: Annotated[ShowQuestionRequest, Path()],
):
    """
    Эндпоинт для получения вопроса по его уникальному идентификатору вместе со всеми ответами.

    Выполняет поиск вопроса в базе данных по `id`. Если вопрос не найден, возвращает ошибку 404.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.
        question_id (ShowQuestionRequest): Идентификатор вопроса, переданный в пути запроса.

    Returns:
        ShowQuestionResponse: Объект, содержащий:
            - `id`: Уникальный идентификатор вопроса.
            - `text`: Текст вопроса.
            - `created_at`: Время создания.
            - `updated_at`: Время последнего обновления.
            - `answers`: Список связанных ответов (модель `Answer`).

    Raises:
        HTTPException: С кодом 404, если вопрос с указанным `id` не найден.
            Текст ошибки берётся из выброшенного `ValueError`.
    """
    try:
        question = await find_question_by_id(session, question_id)
    except ValueError as e:
        raise HTTPException(404, detail=str(e)) from e

    return question
