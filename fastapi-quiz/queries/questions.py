from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message:str

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
    id: int

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

    def get_one(self, q_number: int) -> Optional[QuestionOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT q_number
                        , question
                        , answer1
                        , answer2
                        , answer3
                        , answer4
                        , value1
                        , value2
                        , value3
                        , value4
                        FROM quiz_question_answer
                        WHERE q_number = %s;
                        """,
                        [q_number]
                    )
                    record = result.fetchone()
                    print("record:", record)
                    if record is None:
                        return None
                    return QuestionOut(
                        q_number = record[0],
                        question = record[1],
                        answer1 = record[2],
                        answer2 = record[3],
                        answer3 = record[4],
                        answer4 = record[5],
                        value1 = record[6],
                        value2 = record[7],
                        value3 = record[8],
                        value4 = record[9]
                    )
        except Exception as e:
            print(e)
            return {"message": "dont feel like getting account data rn tbh"}

    def get_all(self) -> Union[List[QuestionOut], Error]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            db.execute(
              """
              SELECT
                    q_number,
                    question,
                    answer1,
                    answer2,
                    answer3,
                    answer4,
                    value1,
                    value2,
                    value3,
                    value4,
                    id
              FROM quiz_question_answer
              ORDER BY q_number;
              """
            )
            result = []
            for record in db:
              question = QuestionOut(
                q_number = record[0],
                question = record[1],
                answer1 = record[2],
                answer2 = record[3],
                answer3 = record[4],
                answer4 = record[5],
                value1 = record[6],
                value2 = record[7],
                value3 = record[8],
                value4 = record[9],
                id =record[10]
              )
              result.append(question)
            return result
      except Exception as e:
        print(e)
        return {"message": "dont forget to call your mom"}

    def delete(self, q_number: int) -> bool:
            try:
                # connect the database
                with pool.connection() as conn:
                    # get a cursor (something to run SQL with)
                    with conn.cursor() as db:
                        db.execute(
                            """
                            DELETE FROM quiz_question_answer
                            WHERE q_number = %s
                            """,
                            [q_number]
                        )
                        return True
            except Exception as e:
                print(e)
                return False

    def update(self, id: int, question: QuestionIn) -> Union[QuestionOut, Error]:
            try:
                with pool.connection() as conn:
                    with conn.cursor() as db:
                        db.execute(
                            """
                            UPDATE quiz_question_answer
                            SET
                              q_number = %s,
                              question = %s,
                              answer1 = %s,
                              answer2 = %s,
                              answer3 = %s,
                              answer4 = %s,
                              value1 = %s,
                              value2 = %s,
                              value3 = %s,
                              value4 = %s
                            WHERE id = %s
                            """,
                            [
                              question.q_number,
                              question.question,
                              question.answer1,
                              question.answer2,
                              question.answer3,
                              question.answer4,
                              question.value1,
                              question.value2,
                              question.value3,
                              question.value4,
                              id
                            ]
                        )

                        return self.question_in_to_out(id, question)
            except Exception as e:
                print(e)
                return {"message": "I wouldn't do that if I were you"}

    def question_in_to_out(self, id:int, question: QuestionIn):
        old_data = question.dict()
        return QuestionOut(id=id, **old_data)