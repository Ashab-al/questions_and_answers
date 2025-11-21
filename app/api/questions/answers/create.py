from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.post(
    "/{id}/answers/",
)
async def create_answers(id: Annotated[int, Path()]):
    ...