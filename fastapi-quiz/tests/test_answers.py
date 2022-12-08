from fastapi.testclient import TestClient
from main import app
from queries.answers import AnswerRepo

client = TestClient(app)
class EmptyAnswerQueries:
    def get_all(self):
        return []

def test_get_all_answers():
    # arrange
    app.dependency_overrides[AnswerRepo] = EmptyAnswerQueries

    # act
    response = client.get("/answers")

    # assert
    assert response.status_code == 200
    assert response.json() == []

    # clean up
    app.dependency_overrides = {}