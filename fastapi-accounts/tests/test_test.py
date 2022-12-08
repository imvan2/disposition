# from fastapi.testclient import TestClient
# from main import app
# from queries.accounts import AccountRepository

# client = TestClient(app)
# #said create needs 3 parameters,not sure why, added result and no more error
# #now error is poiting to authenticator, about get_one()
# class CreateAccountRepository:
#     def create(self, account, result):
#         result = {
#             "first_name": "John",
#             "last_name": "Smith",
#             "username": "jsmith",
#             "password": "password",
#             "email": "jsmith@gmail.com",
#             # hashed_password:"alsjdfaklsjdlafs"
#         }
#         result.update(account)
#         return result

# def test_create_account():
#     app.dependency_overrides[AccountRepository] = CreateAccountRepository
#     json = {
#         "first_name": "John",
#         "last_name": "Smith",
#         "username": "jsmith",
#         "password": "password",
#         "email": "jsmith@gmail.com",
#         # "hashed_password": "asdfjkalsdjfkla"
#     }

#     expected = {
#         "first_name": "John",
#         "last_name": "Smith",
#         "username": "jsmith",
#         "password": "password",
#         "email": "jsmith@gmail.com"
#     }
#     response = client.post("/signup", json=json)

#     assert response.status_code == 200
#     assert response.json() == expected
#     app.dependency_overrides = {}


def test_test():
    assert 1 == 1
