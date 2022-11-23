from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message:str

class PlaylistIn(BaseModel):
    user_id: int
    search_term: str
    playlist_id: str
    name: str
    pic: str
    url: str
    rating: int

class PlaylistOut(BaseModel):
    id: int
    user_id: int
    search_term: str
    playlist_id: str
    name: str
    pic: str
    url: str
    rating: int

class PlaylistRepo:
    def create(self, playlist: PlaylistIn) -> PlaylistOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO playlists
                        (user_id,
                        search_term,
                        playlist_id,
                        name,
                        pic,
                        url,
                        rating)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [playlist.user_id,
                      playlist.search_term,
                      playlist.playlist_id,
                      playlist.name,
                      playlist.pic,
                      playlist.url,
                      playlist.rating]
                )
                id = result.fetchone()[0]
                old_data = playlist.dict()
                return PlaylistOut(id=id, **old_data)


    def delete(self, playlist_id: str) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM playlists
                        WHERE playlist_id = %s
                        """,
                        [playlist_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(self, id: int, playlist: PlaylistIn) -> Union[PlaylistOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE playlists
                        SET
                            user_id = %s,
                            search_term = %s,
                            name = %s,
                            pic = %s,
                            url = %s,
                            playlist_id = %s,
                            rating = %s
                        WHERE id = %s
                        """,
                        [
                            playlist.user_id,
                            playlist.search_term,
                            playlist.name,
                            playlist.pic,
                            playlist.url,
                            playlist.playlist_id,
                            playlist.rating,
                            id
                        ]
                    )
                    return self.record_to_playlist_out(id, playlist)
        except Exception as e:
            print(e)
            return {"message": "Could not update that playlist"}

    def get_all(self) -> Union[List[PlaylistOut],Error]:
            try:
                with pool.connection() as conn:
                    with conn.cursor() as db:
                        db.execute(
                            """
                            SELECT
                                user_id,
                                search_term,
                                playlist_id,
                                name,
                                pic,
                                url,
                                id,
                                rating
                            FROM playlists
                            ORDER BY id;
                            """
                        )
                        result = []
                        for record in db:
                            playlist = PlaylistOut(
                                user_id=record[0],
                                search_term=record[1],
                                playlist_id=record[2],
                                name=record[3],
                                pic=record[4],
                                url = record[5],
                                id = record[6],
                                rating = record[7]
                            )
                            result.append(playlist)
                        return result
            except Exception as e:
                print(e)
                return {"message": "Could not get all playlists"}

    def get_one(self, playlist_id: str) -> Optional[PlaylistOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                          playlist_id,
                          user_id,
                          search_term,
                          name,
                          pic,
                          url,
                          id,
                          rating
                        FROM playlists
                        WHERE playlist_id = %s;
                        """,
                        [playlist_id]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return PlaylistOut(
                        playlist_id=record[0],
                        user_id=record[1],
                        search_term=record[2],
                        name=record[3],
                        pic=record[4],
                        url=record[5],
                        id = record[6],
                        rating = record[7]
                    )
        except Exception as e:
            print(e)
            return {"message": "Get One failed, re-evaluate yourself and try again"}

    def record_to_playlist_out(self, id:int, playlist: PlaylistIn):
        old_data = playlist.dict()
        return PlaylistOut(id=id, **old_data)
