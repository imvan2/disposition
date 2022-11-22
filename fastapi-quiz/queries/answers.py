from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message:str
    
class AnswerIn(BaseModel):
    user_id: int
    q_number: int
    question: str
    answer: str
    value: int
    
class AnswerOut(BaseModel):
    id: int
    user_id: int
    q_number: int
    question: str
    answer: str
    value: int
    
class AnswerRepo:
    def create(self, answer: AnswerIn) -> AnswerOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO quiz_answer
                        (user_id,
                        q_number,
                        question,
                        answer,
                        value)
                    VALUES
                        (%s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [answer.user_id,
                     answer.q_number,
                     answer.question,
                     answer.answer,
                     answer.value]
                )
                id = result.fetchone()[0]
                old_data = answer.dict()
                return AnswerOut(id=id, **old_data)

    def get_all(self) -> Union[List[AnswerOut], Error]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            db.execute(
              """
              SELECT
                    user_id,
                    q_number,
                    question,
                    answer,
                    value,
                    id
              FROM quiz_answer
              ORDER BY q_number;
              """
            )
            result = []
            for record in db:
              answer = AnswerOut(
                user_id = record[0],
                q_number = record[1],
                question = record[2],
                answer = record[3],
                value = record[4],
                id = record[5]
              )
              result.append(answer)
            return result
      except Exception as e:
        print(e)
        return {"message": "dont forget to call your mom"}

    def get_one(self, q_number: int) -> Optional[AnswerOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT 
                          user_id,
                          q_number,
                          question,
                          answer,
                          value,
                          id
                        FROM quiz_answer
                        WHERE q_number = %s;
                        """,
                        [q_number]
                    )
                    record = result.fetchone()
                    print("record:", record)
                    if record is None:
                        return None
                    return AnswerOut(
                        user_id = record[0],
                        q_number = record[1],
                        question = record[2],
                        answer = record[3],
                        value = record[4],
                        id = record[5]
                    )
        except Exception as e:
            print(e)
            return {"message": "did you expect something different?"}
                    
                         
    def delete(self, q_number: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            DELETE FROM quiz_answer
                            WHERE q_number = %s
                            """,
                            [q_number]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(self, id: int, answer: AnswerIn) -> Union[AnswerOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE quiz_answer
                        SET
                            q_number = %s,
                            question = %s,
                            answer = %s,
                            value = %s
                        WHERE id = %s
                        """,
                        [
                        answer.q_number,
                        answer.question,
                        answer.answer,
                        answer.value,
                        id
                        ]
                    )

                    return self.answer_in_to_out(id, answer)
        except Exception as e:
            print(e)
            return {"message": "Are you sure?"}

    def answer_in_to_out(self, id:int, answer: AnswerIn):
        old_data = answer.dict()
        return AnswerOut(id=id, **old_data)