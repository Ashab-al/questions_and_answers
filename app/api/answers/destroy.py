from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, Body, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.answers.destroy_answer_by_id import destroy_answer_by_id

router = APIRouter()

@router.delete(
    "/{answer_id}",
)
async def destroy(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    answer_id: Annotated[int, Path()],
):
    try:
        answer = await destroy_answer_by_id(session, answer_id)
    except ValueError as e:
        raise HTTPException(404, str(e)) from e

    return answer