from sqlalchemy import Column, String, Integer
from database import Base


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)

    ids = Column(Integer)

    q_text = Column(String)

    q_answer = Column(String)

    created_date = Column(String)
