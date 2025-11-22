from fastapi import APIRouter
from api.questions.answers.create import router as answers_create_router

router = APIRouter()

router.include_router(answers_create_router, tags=["Answers"])