from fastapi.testclient import TestClient
from main import app
from queries.questions import QuestionRepo

client= TestClient(app)

class CreateQuestionRepository:
    def create(self, question):
        result = {
                "q_number": 0,
                "question": "What's your fav food?",
                "answer1": "Ramen",
                "answer2": "Sushi",
                "answer3": "Tacos",
                "answer4": "Socks",
                "value1": 0,
                "value2": 1,
                "value3": 2,
                "value4": 3,
                "id": 1
        }
        result.update(question)
        return result

def test_create_question():
    app.dependency_overrides[QuestionRepo] = CreateQuestionRepository
    json = {
            "q_number": 0,
            "question": "What's your fav food?",
            "answer1": "Ramen",
            "answer2": "Sushi",
            "answer3": "Tacos",
            "answer4": "Socks",
            "value1": 0,
            "value2": 1,
            "value3": 2,
            "value4": 3
    }

    expected = {
            "q_number": 0,
            "question": "What's your fav food?",
            "answer1": "Ramen",
            "answer2": "Sushi",
            "answer3": "Tacos",
            "answer4": "Socks",
            "value1": 0,
            "value2": 1,
            "value3": 2,
            "value4": 3,
            "id": 1
        }
    response = client.post("/questions", json=json)

    assert response.status_code == 200
    assert response.json() == expected
    app.dependency_overrides = {}



# class EmptyQuestionRepo:
#     def get_one_question(self, q_number):
#         return None

# def test_get_one_question():
# # Arrange
#     app.dependency_overrides[QuestionRepo] = EmptyQuestionRepo
#     q_number = 1
# # Act
#     response = client.get("/questions/{q_number}")
# # Assert
#     assert response.status_code == 200
#     assert response.json() == None
# # Clean up
#     app.dependency_overides = {}