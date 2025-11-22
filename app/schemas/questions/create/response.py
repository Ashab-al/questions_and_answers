from pydantic import BaseModel
from pydantic import Field
from datetime import datetime

class CreateQuestionResponse(BaseModel):
    id: int = Field(..., examples=[1], title="ID вопроса")
    created_at: datetime = Field(..., examples=["2023-10-05T14:48:00Z"], title="Время создания вопроса")
    updated_at: datetime = Field(..., examples=["2023-10-05T14:48:00Z"], title="Время последнего обновления вопроса")
    text: str = Field(..., examples=[["Какой-то вопрос"]], title="Текст вопроса", max_length=500, min_length=1)
