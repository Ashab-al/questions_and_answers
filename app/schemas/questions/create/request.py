from pydantic import BaseModel
from pydantic import Field

class CreateQuestionRequest(BaseModel):
    text: str = Field(..., examples=["Какой-то вопрос"], title="Текст вопроса", max_length=500, min_length=1)
