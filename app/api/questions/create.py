from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.create.request import CreateQuestionRequest
from schemas.questions.create.response import CreateQuestionResponse
from services.questions.create_question import create_questions


router = APIRouter()
@router.post(
    "/",
    summary="Создать новый вопрос",
    description="Создает новый вопрос в базе данных.",
    response_model=CreateQuestionResponse,
)
async def create(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    create_question: Annotated[CreateQuestionRequest, Body()],
):
    question = await create_questions(
        session=session,
        create_question=create_question,
    )

    return CreateQuestionResponse(
        id=question.id,
        text=question.text,
        created_at=question.created_at,
        updated_at=question.updated_at
    )
