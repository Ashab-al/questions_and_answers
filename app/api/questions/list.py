from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.list.response import ListQuestionsResponse
from services.questions.list_questions import list_questions


router = APIRouter()
@router.get(
    "/",
    summary="Получить список всех вопросов",
    description="Возвращает список всех вопросов в базе данных.",
    response_model=ListQuestionsResponse,
)
async def questions_list(
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    """
    Получить список всех вопросов

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с базой данных.

    Returns:
        ListQuestionsResponse: Объект, содержащий список всех вопросов
    """
    questions = await list_questions(session)

    return ListQuestionsResponse(questions=questions)
