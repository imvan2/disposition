from pydantic import BaseModel
from typing import Optional
from queries.pool import pool

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
            #run our insert statement, give them an order after

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
                account.email
              ]
            )
            id = result.fetchone()[0]
            old_data = account.dict()
            return AccountOut(id=id, **old_data)