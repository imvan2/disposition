from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

from psycopg import connect
import os

keepalive_kwargs = {
    "keepalives": 1,
    "keepalives_idle": 60,
    "keepalives_interval": 10,
    "keepalives_count": 5,
}

class Error(BaseModel):
    message:str
    
class BillboardIn(BaseModel):
    rank: int
    title: str
    artist: str
    album_pic:str

class BillboardOut(BaseModel):
    rank: int
    title: str
    artist: str
    album_pic:str
    
class BillboardRepo:
    def create_billboard(self, billboard: BillboardIn):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO billboard
                        (rank,
                        title,
                        artist,
                        album_pic)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING rank;
                    """,
                    [billboard["rank"],
                    billboard["title"],
                    billboard["artist"],
                    billboard["album_pic"]]
                )
                rank = result.fetchone()[0]
                return billboard
    
    def get_all(self):
        try:
            with connect(
                conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs
            ) as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT
                            rank,
                            title,
                            artist,
                            album_pic
                        FROM billboard
                        ORDER BY rank;
                        """
                    )
                    results = []
                    for item in db:
                        song = BillboardOut(
                            rank = item[0],
                            title = item[1],
                            artist = item[2],
                            album_pic = item[3],
                        )
                        results.append(song)
                    return results
        except Exception as e:
            print(e)
            
    def delete(self, rank: int) -> bool:
        try:
            with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs) as conn:
                with conn.cursor() as db:
                    
                    db.execute(
                        """
                        DELETE FROM billboard
                        WHERE rank = %s
                        """,
                        [rank],
                    )
                    print("db:", db)
                    return True
        except Exception as e:
            print(e)