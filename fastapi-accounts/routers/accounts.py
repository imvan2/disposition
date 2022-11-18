from fastapi import APIRouter, Depends, Response
from queries.accounts import (
  AccountIn,
  AccountRepository,
  AccountOut,
  Error)
from typing import Union, List, Optional

router = APIRouter()


@router.post("/signup", response_model=Union[AccountOut, Error])
def create_account(account: AccountIn, repo: AccountRepository = Depends()):
    return repo.create(account)


@router.get("/accounts", response_model=Union[Error, List[AccountOut]])
def get_all(repo: AccountRepository = Depends()):
    return repo.get_all()


@router.delete("/accounts/{id}", response_model=bool)
def del_account(
    id: int,
    repo: AccountRepository = Depends(),
) -> bool:
    return repo.delete(id)

@router.get("/accounts/{id}", response_model=Optional[AccountOut])
def get_one_account(
  id: int,
  response: Response,
  repo: AccountRepository = Depends(),
) -> AccountOut:
  account = repo.get_one(id)
  if account is None:
    response.status_code = 404
  return account
