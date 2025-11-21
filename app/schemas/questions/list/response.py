from pydantic import BaseModel
from pydantic import Field, ConfigDict
from datetime import datetime

class Answer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., examples=[1], description="ID ответа")
    question_id: int = Field(..., examples=[1], description="ID вопроса, к которому относится ответ")
    user_id: str = Field(..., examples=["550e8400-e29b-41d4-a716-446655440000"], description="ID пользователя, создавшего ответ")
    text: str = Field(..., examples=[["Какой-то ответ"]], description="Текст ответа")

class Question(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., examples=[1], description="ID вопроса")
    created_at: datetime = Field(..., description="Время создания вопроса")
    updated_at: datetime = Field(..., description="Время последнего обновления вопроса")
    text: str = Field(..., examples=[["Какой-то вопрос"]], description="Текст вопроса")
    answers: list[Answer] = Field(..., description="Список ответов на вопрос")

class ListQuestionsResponse(BaseModel):
    questions: list[Question] = Field(..., description="Список вопросов")
