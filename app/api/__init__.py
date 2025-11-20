from fastapi import APIRouter
from api.questions import questions_router
api_router = APIRouter()

api_router.include_router(questions_router, prefix="/questions", tags=["Questions"])