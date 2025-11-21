from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.delete(
    "/{id}",
)
async def destroy(id: Annotated[int, Path()]):
    ...