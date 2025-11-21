from schemas.questions.create.request import CreateQuestionRequest
from sqlalchemy.ext.asyncio import AsyncSession
from models.question import Question

async def create_questions(
    session: AsyncSession,
    create_question: CreateQuestionRequest,
):
    question: Question = Question(text=create_question.text)

    session.add(question)

    await session.commit()
    await session.refresh(question)

    return question
