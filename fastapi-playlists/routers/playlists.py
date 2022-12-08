from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union


from queries.playlists import (
    Error,
    PlaylistIn,
    PlaylistRepo,
    PlaylistOut,
)

router = APIRouter()
# where this file is stored


@router.post("/playlists", response_model=PlaylistOut)
def create_playlist(playlist: PlaylistIn, repo: PlaylistRepo = Depends()):
    return repo.create(playlist)


@router.get("/playlists", response_model=Union[List[PlaylistOut], Error])
def get_all(
    repo: PlaylistRepo = Depends(),
):
    print("playlistgetall:", repo.get_all())
    return repo.get_all()


@router.put("/playlists/{id}", response_model=Union[PlaylistOut, Error])
def update_playlist(
    id: int,
    playlist: PlaylistIn,
    repo: PlaylistRepo = Depends(),
) -> Union[Error, PlaylistOut]:
    return repo.update(id, playlist)


@router.delete("/playlists/{playlist_id}", response_model=bool)
def delete_playlist(
    playlist_id: str,
    repo: PlaylistRepo = Depends(),
) -> bool:
    return repo.delete(playlist_id)


@router.get("/playlists/{playlist_id}", response_model=Optional[PlaylistOut])
def get_one_playlist(
    playlist_id: str,
    response: Response,
    repo: PlaylistRepo = Depends(),
) -> PlaylistOut:
    playlist = repo.get_one(playlist_id)
    if playlist is None:
        response.status_code = 404
    return playlist
