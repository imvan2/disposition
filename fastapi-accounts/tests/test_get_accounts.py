# from fastapi.testclient import TestClient
# from main import app
# from queries.accounts import AccountRepository

# client= TestClient(app)

# class EmptyAccountsRepo:
#     def get_all(self):
#         return []

# def test_get_all_accounts():
# # Arrange
#     app.dependency_overrides[AccountRepository] = EmptyAccountsRepo
# # Act
#     response = client.get("/accounts")
# # Assert
#     assert response.status_code == 200
#     assert response.json() == []
# # Clean up
#     app.dependency_overides = {}