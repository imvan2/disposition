from fastapi.testclient import TestClient
from main import app
from queries.questions import QuestionRepo

client = TestClient(app)


class EmptyQuestionsQueries:
    def get_all(self):
        return []


def test_get_all_questions():
    # arrange
    app.dependency_overrides[QuestionRepo] = EmptyQuestionsQueries

    # act
    response = client.get("/questions")

    # assert
    assert response.status_code == 200
    assert response.json() == []

    # clean up
    app.dependency_overrides = {}
