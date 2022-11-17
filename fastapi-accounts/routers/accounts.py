from fastapi import APIRouter, Depends
from queries.accounts import AccountIn, AccountRepository, AccountOut

router = APIRouter()


@router.post("/signup", response_model = AccountOut)
def create_account(
  account: AccountIn,
  repo: AccountRepository = Depends()
  ):
  return repo.create(account)