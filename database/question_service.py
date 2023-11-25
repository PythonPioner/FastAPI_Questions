from database.models import Question

from database import get_db


def checker_question_id_db(id_question: int):
    db = next(get_db())

    question = db.query(Question).filter_by(ids=id_question).first()

    if question:
        return True

    return False


def add_question_to_db(ids: int, question: str, answer: str, date: str):
    db = next(get_db())

    question = Question(
        ids=ids,
        q_text=question,
        q_answer=answer,
        created_date=date
    )

    db.add(question)
    db.commit()


def get_any_question(count: int):

    db = next(get_db())

    # question = db.query(Question).all()
    any_question = db.query(Question).order_by(Question.id.desc()).limit(count).all()

    return any_question

