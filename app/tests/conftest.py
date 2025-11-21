import sys
from pathlib import Path
from unittest.mock import AsyncMock

import pytest
import pytest_asyncio

# Добавляем импорт модули Questions
from api.questions import questions_router
from api.questions import create as questions_create_module
from api.questions import destroy as questions_destroy_module
from api.questions import list as questions_list_module
from api.questions import show as questions_show_module


from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

async def remove_response_model_in_router(router):
    """Убираем response_model из роутеров"""
    for route in router.routes:
        route.response_model = None
    return router

@pytest_asyncio.fixture
async def app(session_mock: AsyncMock) -> FastAPI:  # noqa: W0621
    """Создаем тестовый FastAPI app"""
    new_app = FastAPI()

    new_app.include_router(
        await remove_response_model_in_router(questions_router), prefix="/questions"
    )



    async def _override_get_async_session():
        """Мокаем зависимость get_async_session"""
        yield session_mock

    new_app.dependency_overrides[questions_create_module.get_async_session] = (
        _override_get_async_session
    )

    new_app.dependency_overrides[questions_destroy_module.get_async_session] = (
        _override_get_async_session
    )

    new_app.dependency_overrides[questions_list_module.get_async_session] = (
        _override_get_async_session
    )

    new_app.dependency_overrides[questions_show_module.get_async_session] = (
        _override_get_async_session
    )

    return new_app

@pytest.fixture
def session_mock() -> AsyncMock:
    """Мокаем сессию"""
    return AsyncMock()

@pytest_asyncio.fixture
async def client(app: FastAPI):
    """Создаем тестовый клиент для FastAPI app"""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client