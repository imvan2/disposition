from pydantic import BaseModel
from typing import Optional
from queries.pool import pool

class QuestionIn(BaseModel):
    q_number: int
    question: str
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    value1: int
    value2: int
    value3: int
    value4: int

class QuestionOut(BaseModel):
    q_number: int
    question: str
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    value1: int
    value2: int
    value3: int
    value4: int

class QuestionRepo:
    def create(self, question: QuestionIn) -> QuestionOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO quiz_question_answer
                        (q_number,
                        question,
                        answer1,
                        answer2,
                        answer3,
                        answer4,
                        value1,
                        value2,
                        value3,
                        value4)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [question.q_number,
                     question.question,
                     question.answer1,
                     question.answer2,
                     question.answer3,
                     question.answer4,
                     question.value1,
                     question.value2,
                     question.value3,
                     question.value4]
                )
                id = result.fetchone()[0]
                old_data = question.dict()
                return QuestionOut(id=id, **old_data)