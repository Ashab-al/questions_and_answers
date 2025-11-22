from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, Body, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.answers.find_answer_by_id import find_answer_by_id

router = APIRouter()

@router.get(
    "/{answer_id}",
)
async def show(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    answer_id: Annotated[int, Path()]
):
    try:
        answer = await find_answer_by_id(session, answer_id)
    except ValueError as e:
        raise HTTPException(404, str(e)) from e

    return answer
