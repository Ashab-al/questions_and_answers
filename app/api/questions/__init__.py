from api.questions.show import router as show_router
from api.questions.list import router as list_router
from api.questions.create import router as create_router
from api.questions.destroy import router as destroy_router
from api.questions.answers import router as answers_router
from fastapi import APIRouter

questions_router = APIRouter()

questions_router.include_router(show_router)
questions_router.include_router(list_router)
questions_router.include_router(create_router)
questions_router.include_router(destroy_router)
questions_router.include_router(answers_router)
