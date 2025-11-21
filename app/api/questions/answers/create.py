from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, Body, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.answers.create.request import CreateAnswerRequest
from services.questions.answers.create_answer import create_answer
router = APIRouter()

@router.post(
    "/{question_id}/answers/",
)
async def create(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    question_id: Annotated[int, Path()],
    answer_data: Annotated[CreateAnswerRequest, Body()]
):
    try:
        answer = await create_answer(session, question_id, answer_data)
    except ValueError as e:
        raise HTTPException(404, str(e)) from e

    return answer
