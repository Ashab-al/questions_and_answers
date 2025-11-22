from fastapi import APIRouter
from api.questions import questions_router
from api.answers import router as answers_router

api_router = APIRouter()

api_router.include_router(questions_router, prefix="/questions", tags=["Questions"])
api_router.include_router(answers_router, prefix="/answers", tags=["Answers"])
