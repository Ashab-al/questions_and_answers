# API-сервис для вопросов и ответов

## Структура проекта
```
project/
├── app/
│   ├── api/
│   ├── migration/
│   ├── models/
│   ├── query_objects/
│   ├── schemas/
│   ├── services/
│   ├── tests/
│   ├── config.py
│   ├── database.py
│   └── main.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── requirements.txt

```
### Каталоги, содержащиеся в проекте:
- `app` - Корневая директория с кодом приложения.
- `api` - Роутеры (эндпоинты), разбитые по модулям.
- `migration` - Файлы миграций Alembic.
- `models` - SQLAlchemy модели и их связи.
- `query_objects` - Содержит объекты запросов в базу данных.
- `schemas` - Pydantic-схемы для валидации входящих данных и формирования ответов.
- `services` - Содержит бизнес логику.
- `tests` - Содержит все тесты

### Файлы, содержащиеся в проекте:
- `config.py` - Конфигурация приложения
- `database.py` - Подключение к базе данных, создание сессий, engine.
- `main.py` - Точка входа в приложение

## Стек технологий
- Python 3.13+
- Асинхронное программирование: asyncio, asyncpg
- Web / API: FastAPI
- База данных: PostgreSQL, SQLAlchemy ORM, Alembic для миграций
- Валидация и конфигурация: Pydantic, pydantic-settings
- Тестирование: Pytest
- Управление окружением: Docker / Docker Compose

## Установка и запуск проекта
#### Следуйте этим шагам, чтобы запустить проект на своем устройстве:

### 1. Подготовка .env
Перед запуском локального проекта:

``` bash
cp .env.example .env
```
Заполните переменные в .env

### 2. Запуск через Docker Compose:
| Файл         | Назначение                            | Пример запуска                |
|--------------|----------------------------------------|-------------------------------|
| `docker-compose.yml`       | **Разработка** | `docker compose up --build`   |

#### Остановить приложение (`Ctrl + C`) либо:
```
docker compose stop
```

### 3. Миграции
Создать новую миграцию:
```
docker compose run --rm web alembic revision --autogenerate -m "new migration"
```
Применить миграции:
```
docker compose run --rm web alembic upgrade head
```

### 4. Тесты
Запуск тестов:
```
pytest .
```
