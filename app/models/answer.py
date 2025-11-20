from models.base import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Answer(Base):
    """
    Модель `Answer` в базе данных.

    Атрибуты:
        id (int): Уникальный идентификатор ответа. Первичный ключ таблицы.
        question_id (int): Идентификатор вопроса, к которому относится ответ.
                           Является внешним ключом, ссылающимся на таблицу `questions`.

        question (Question): Связь "обратное отношение" к объекту `Question`.
                             Позволяет получать вопрос, к которому относится ответ.
                             Обратное поле в `Question` называется `answers`.
    """

    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))

    question = relationship("Question", back_populates="answers", nullable=False)
