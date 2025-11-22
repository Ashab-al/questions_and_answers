from pydantic import BaseModel
from pydantic import Field
import uuid

class CreateAnswerRequest(BaseModel):
    text: str = Field(..., description="Текст ответа на вопрос", examples=["Какой-то вопрос"])
    user_id: str = Field(..., description="id пользователя uuid", examples=[str(uuid.uuid4())])
