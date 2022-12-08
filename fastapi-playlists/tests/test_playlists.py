from fastapi.testclient import TestClient
from main import app
from queries.playlists import PlaylistRepo

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_all(self):
        return []


def test_get_all_playlists():
    # arrange
    app.dependency_overrides[PlaylistRepo] = EmptyPlaylistQueries

    # act
    response = client.get("/playlists")

    # assert
    assert response.status_code == 200
    assert response.json() == []

    # clean up
    app.dependency_overrides = {}
