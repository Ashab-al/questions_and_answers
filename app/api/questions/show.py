from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
@router.get(
    "/{question_id}",
    summary="Получить вопрос и все ответы на него",
    description="Возвращает вопрос по его ID вместе со всеми связанными ответами.",
)
async def show_question(
    question_id: Annotated[int, Path()],
):
    ...