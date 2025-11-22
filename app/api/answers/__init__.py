
from api.answers.show import router as show_router
from api.answers.destroy import router as destroy_router


from fastapi import APIRouter

router = APIRouter()

router.include_router(show_router)
router.include_router(destroy_router)
