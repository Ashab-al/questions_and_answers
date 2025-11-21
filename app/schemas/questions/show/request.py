from pydantic import BaseModel
from pydantic import Field, ConfigDict


class ShowQuestionRequest(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор вопроса.", examples=[1])
