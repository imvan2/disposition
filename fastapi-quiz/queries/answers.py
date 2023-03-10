from pydantic import BaseModel
from typing import Optional, List, Union

# from queries.pool import pool
from psycopg import connect
import os


class Error(BaseModel):
    message: str


class AnswerIn(BaseModel):
    user_id: int
    mood: str
    genre: str


class AnswerOut(BaseModel):
    id: int
    user_id: int
    mood: str
    genre: str


keepalive_kwargs = {
    "keepalives": 1,
    "keepalives_idle": 60,
    "keepalives_interval": 10,
    "keepalives_count": 5,
}


class AnswerRepo:
    def create(self, answer: AnswerIn) -> AnswerOut:
        with connect(
            conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
        ) as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO quiz_answer
                        (user_id,
                        mood,
                        genre)
                    VALUES
                        (%s, %s, %s)
                    RETURNING id;
                    """,
                    [answer.user_id, answer.mood, answer.genre],
                )
                id = result.fetchone()[0]
                old_data = answer.dict()
                return AnswerOut(id=id, **old_data)

    def get_all(self) -> Union[List[AnswerOut], Error]:
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
              SELECT
                    user_id,
                    mood,
                    genre,
                    id
              FROM quiz_answer
              ORDER BY id;
              """
                    )
                    result = []
                    print("db:::", db)
                    for record in db:
                        print("record::", record)
                        answer = AnswerOut(
                            user_id=record[0],
                            mood=record[1],
                            genre=record[2],
                            id=record[3],
                        )
                        result.append(answer)
                    return result
        except Exception as e:
            print(e)
            return {"message": "dont forget to call your mom"}

    def get_one(self, id: int) -> Optional[AnswerOut]:
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                          user_id,
                          mood,
                          genre
                        FROM quiz_answer
                        WHERE id = %s;
                        """,
                        [id],
                    )
                    record = result.fetchone()
                    print("record:", record)
                    if record is None:
                        return None
                    return AnswerOut(
                        user_id=record[0],
                        mood=record[1],
                        genre=record[2],
                        id=record[3],
                    )
        except Exception as e:
            print(e)
            return {"message": "did you expect something different?"}

    def delete(self, id: int) -> bool:
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            DELETE FROM quiz_answer
                            WHERE id = %s
                            """,
                        [id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(self, id: int, answer: AnswerIn) -> Union[AnswerOut, Error]:
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE quiz_answer
                        SET
                            mood = %s,
                            genre = %s
                        WHERE id = %s
                        """,
                        [answer.mood, answer.genre, id],
                    )

                    return self.answer_in_to_out(id, answer)
        except Exception as e:
            print(e)
            return {"message": "Are you sure?"}

    def answer_in_to_out(self, id: int, answer: AnswerIn):
        old_data = answer.dict()
        return AnswerOut(id=id, **old_data)
