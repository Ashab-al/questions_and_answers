from models.base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Question(Base):
    """
    Модель `Question` в базе данных.

    Атрибуты:
        id (int): Уникальный идентификатор вопроса. Первичный ключ таблицы.
        text (str): Текст вопроса, ограниченный 1000 символами. Не может быть пустым (nullable=False).

        answers (list[Answer]): Список связанных ответов.
                                Отношение настроено с каскадным удалением:
                                - `all`: Все операции (add, merge и т.д.) передаются связанным объектам.
                                - `delete-orphan`: Если ответ отвязан от вопроса, он будет удалён из БД.
    """

    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(1000), nullable=False)

    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan") # удалить все answers при удалении вопроса
