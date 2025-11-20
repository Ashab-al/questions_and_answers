from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
@router.post(
    "/",
    summary="Создать новый вопрос",
    description="Создает новый вопрос в базе данных.",
)
async def create_questions(text: Annotated[str, Body()]):
    ...