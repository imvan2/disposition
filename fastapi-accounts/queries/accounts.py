from pydantic import BaseModel
from typing import List, Optional, Union
# from queries.pool import pool
from psycopg import connect
import os

keepalive_kwargs = {
   "keepalives": 1,
   "keepalives_idle": 60,
   "keepalives_interval": 10,
   "keepalives_count": 5
  }

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
    # password: str
    email: str

class Account(BaseModel):
  id: int
  first_name: str
  last_name: str
  username: str
  hashed_password: str
  email: str



class AccountRepository:
    def create(self, account: AccountIn, hashed_password: str) -> Account:
        # create a pool of connections to connect the database (hello is someone there)
        # with pool.connection() as conn:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:

            # get a cursor(something to run SQL with), someone picks up the phone
            # with lets us not use try blocks
            with conn.cursor() as db:

                # run our insert statement, give them an order after

                result = db.execute(
                    """
                INSERT INTO accounts
                  (first_name, last_name, username, hashed_password, email)
                VALUES
                  (%s, %s, %s, %s, %s)
                RETURNING id;
              """,
                    [
                        account.first_name,
                        account.last_name,
                        account.username,
                        hashed_password,
                        account.email,
                    ],
                )
                id = result.fetchone()[0]
                old_data = account.dict()
                return AccountOut(id=id, **old_data)

    def get_all(self) -> Union[List[AccountOut], Error]:
      try:
        # with pool.connection() as conn:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
          with conn.cursor() as db:
            db.execute(
              """
              SELECT id, first_name, last_name, username, email
              FROM accounts
              ORDER BY id;
              """
            )
            result = []
            for record in db:
              account = AccountOut(
                id = record[0],
                first_name = record[1],
                last_name = record[2],
                username = record[3],
                email = record[4]
              )
              result.append(account)
            return result
      except Exception as e:
        print(e)
        return {"message": "made you look"}

    def delete(self, id: int) -> bool:
      try:
        # with pool.connection() as conn:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
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


    def get_one(self, username: str) -> Optional[Account]:
      try:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
        # with pool.connection() as conn:
          with conn.cursor() as db:
            result = db.execute(
              """
              SELECT id
                , first_name
                , last_name
                , username
                , hashed_password
                , email
              FROM accounts
              WHERE username = %s;
              """,
              [username]
            )
            record = result.fetchone()
            print("record:", record)
            if record is None:
              return None
            return Account(
              id=record[0],
              first_name=record[1],
              last_name=record[2],
              username=record[3],
              hashed_password=record[4],
              email=record[5]
              )
      except Exception as e:
        print(e)
        return {"message": "dont feel like getting account data rn tbh"}

    def update(self, id:int, account: AccountIn) -> Union[AccountOut, Error]:
      try:
        with connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)  as conn:
        # with pool.connection() as conn:
          with conn.cursor() as db:
            db.execute(
              """
              UPDATE accounts
              SET first_name = %s
              , last_name = %s
              , username = %s
              , email = %s
              WHERE id = %s
              """,
              [
                account.first_name,
                account.last_name,
                account.username,
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
        email = record[4],
      )
