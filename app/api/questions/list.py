from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
@router.get(
    "/",
    summary="Возвращает список всех вопросов",
    description="Возвращает список всех вопросов в базе данных.",
)
async def list_questions():
    ...