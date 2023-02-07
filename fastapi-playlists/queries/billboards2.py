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
                print("billboard:", billboard)
                result = db.execute(
                    """
                    INSERT INTO billboard
                        (rank,
                        title,
                        artist,
                        album_pic)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [billboard.rank,
                    billboard.title,
                    billboard.artist,
                    billboard.album_pic]
                    )
                id = result.fetchone()[0]
                old_data = billboard.dict()
                return BillboardOut(id=id, **old_data)
    
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
                    print("db:", db)
                    results = []
                    for song in db:
                        print("song in queries:", song)
                    return results
        except Exception as e:
            print(e)