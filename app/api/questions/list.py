from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.list.response import ListQuestionsResponse
from services.questions.list_questions import list_questions


router = APIRouter()
@router.get(
    "/",
    summary="Возвращает список всех вопросов",
    description="Возвращает список всех вопросов в базе данных.",
    response_model=ListQuestionsResponse,
)
async def questions_list(
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    questions = await list_questions(session)
    print(questions)
    return ListQuestionsResponse(questions=questions)
