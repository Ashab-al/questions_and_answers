from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
@router.delete(
    "/{question_id}",
    summary="Удалить вопрос",
    description="Удаляет вопрос по его ID из базы данных.",
)
async def create_questions(question_id: Annotated[int, Path()]):
    ...