from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool

class Error(BaseModel):
    message:str

class AccountIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class AccountOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class AccountRepository:
    def create(self, account: AccountIn) -> AccountOut:
        # create a pool of connections to connect the database (hello is someone there)
        with pool.connection() as conn:

            # get a cursor(something to run SQL with), someone picks up the phone
            # with lets us not use try blocks
            with conn.cursor() as db:
                # run our insert statement, give them an order after

                result = db.execute(
                    """
                INSERT INTO accounts
                  (first_name, last_name, username, password, email)
                VALUES
                  (%s, %s, %s, %s, %s)
                RETURNING id;
              """,
                    [
                        account.first_name,
                        account.last_name,
                        account.username,
                        account.password,
                        account.email,
                    ],
                )
                id = result.fetchone()[0]
                old_data = account.dict()
                return AccountOut(id=id, **old_data)

    def get_all(self) -> Union[Error, List[AccountOut]]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            db.execute(
              """
              SELECT id, first_name, last_name, username, password, email
              FROM accounts
              ORDER BY id;
              """
            )
            result = []
            for record in db:
              print("record", record)
              account = AccountOut(
                id = record[0],
                first_name = record[1],
                last_name = record[2],
                username = record[3],
                password = record[4],
                email = record[5]
              )
              result.append(account)
            return result
      except Exception as e:
        print(e)
        return {"message": "made you look"}

    def delete(self, id: int) -> bool:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            db.execute(
              """
                DELETE FROM accounts
                WHERE id = %s
              """,
              [id]
            )
            return True
      except Exception as e:
        return False


    def get_one(self, id: int) -> Optional[AccountOut]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            result = db.execute(
              """
              SELECT id
                , first_name
                , last_name
                , username
                , password
                , email
              FROM accounts
              WHERE id = %s;
              """,
              [id]
            )
            record = result.fetchone()
            if record is None:
              return None
            return self.record_to_account_out(record)
      except Exception as e:
        print(e)
        return {"message": "dont feel like getting account data rn tbh"}

    def update(self, id:int, account: AccountIn) -> Union[AccountOut, Error]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            db.execute(
              """
              UPDATE accounts
              SET first_name = %s
              , last_name = %s
              , username = %s
              , password = %s
              , email = %s
              WHERE id = %s
              """,
              [
                account.first_name,
                account.last_name,
                account.username,
                account.password,
                account.email,
                id
              ]
            )
            print(self.account_in_to_out(id,account))
            return self.account_in_to_out(id,account)
      except Exception as e:
        return {"message":  e}





    def account_in_to_out(self, id:int, account: AccountIn):
        old_data = account.dict()
        return AccountOut(id=id, **old_data)

    def record_to_account_out(self, record):
      return AccountOut(
        id = record[0],
        first_name = record[1],
        last_name = record[2],
        username = record[3],
        password = record[4],
        email = record[5],
      )
