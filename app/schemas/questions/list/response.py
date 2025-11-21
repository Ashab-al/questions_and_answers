from pydantic import BaseModel
from pydantic import Field, ConfigDict
from datetime import datetime

class Answer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., examples=[1], title="ID ответа")
    question_id: int = Field(..., examples=[1], title="ID вопроса, к которому относится ответ")
    user_id: str = Field(..., examples=["550e8400-e29b-41d4-a716-446655440000"], title="ID пользователя, создавшего ответ")
    text: str = Field(..., examples=[["Какой-то ответ"]], title="Текст ответа")

class Question(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., examples=[1], title="ID вопроса")
    created_at: datetime = Field(..., examples=["2023-10-05T14:48:00Z"], title="Время создания вопроса")
    updated_at: datetime = Field(..., examples=["2023-10-05T14:48:00Z"], title="Время последнего обновления вопроса")
    text: str = Field(..., examples=[["Какой-то вопрос"]], title="Текст вопроса")
    answers: list[Answer] = Field(..., title="Список ответов на вопрос")

class ListQuestionsResponse(BaseModel):
    questions: list[Question] = Field(..., title="Список вопросов")