from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message:str

class BillboardIn(BaseModel):
    id: int
    rank: int
    title: str
    artist: str
    album: str


class BillboardOut(BaseModel):
    id: int
    rank: int
    title: str
    artist: str
    album: str


class BillboardRepo:
    # def create_billboard(self, billboard: BillboardIn):
    #     with pool.connection() as conn:
    #         with conn.cursor() as db:
    #             result = db.execute(
    #                 """
    #                 INSERT INTO billboard
    #                     (id,
    #                     rank,
    #                     title,
    #                     artist,
    #                     album)
    #                 VALUES
    #                     (%s, %s, %s, %s, %s)
    #                 RETURNING id;
    #                 """,
    #                 [billboard.id,
    #                   billboard.rank,
    #                   billboard.title,
    #                   billboard.artist,
    #                   billboard.album]
    #             )
    #             id = result.fetchone()[0]
    #             old_data = billboard.dict()
    #             return BillboardOut(id=id, **old_data)

    def get_all(self) -> Union[List[BillboardOut],Error]:
            try:
                with pool.connection() as conn:
                    with conn.cursor() as db:
                        db.execute(
                            """
                            SELECT
                                id,
                                rank,
                                title,
                                artist,
                                album
                            FROM billboard
                            ORDER BY rank;
                            """
                        )
                        result = []
                        for record in db:
                            print("db:::::::",db)
                            billboard = BillboardOut(
                                id=record[0],
                                rank=record[1],
                                title=record[2],
                                artist=record[3],
                                album=record[4]
                            )
                            result.append(billboard)
                        return result
            except Exception as e:
                print(e)
                return {"message": "Could not get all playlists"}