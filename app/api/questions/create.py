from typing import Annotated

from database import get_async_session
from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.questions.create.request import CreateQuestionRequest
from schemas.questions.create.response import CreateQuestionResponse
from services.questions.create_question import create_question


router = APIRouter()
@router.post(
    "/",
    summary="Создать новый вопрос",
    description="Создает новый вопрос в базе данных.",
    response_model=CreateQuestionResponse,
)
async def create(
    session: Annotated[AsyncSession, Depends(get_async_session)],
    question: Annotated[CreateQuestionRequest, Body()],
):
    """
    Эндпоинт для создания нового вопроса.

    Принимает текст вопроса, сохраняет его в базе данных и возвращает объект с данными созданного вопроса.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy, предоставляемая через зависимость.
        create_question (CreateQuestionRequest): Тело запроса, содержащее данные для создания вопроса.
            Ожидается JSON с полем `text` (текст вопроса).

    Returns:
        CreateQuestionResponse: Объект с информацией о созданном вопросе, включая:
            - `id`: Уникальный идентификатор вопроса.
            - `text`: Текст вопроса.
            - `created_at`: Время создания.
            - `updated_at`: Время последнего обновления (совпадает с `created_at` при создании).
    """
    new_question = await create_question(
        session=session,
        new_question=question,
    )

    return CreateQuestionResponse(
        id=new_question.id,
        text=new_question.text,
        created_at=new_question.created_at,
        updated_at=new_question.updated_at
    )
