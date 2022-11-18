from fastapi import APIRouter, Depends
from queries.accounts import (
  AccountIn, 
  AccountRepository, 
  AccountOut,
  Error)
from typing import Union, List

router = APIRouter()


@router.post("/signup", response_model=Union[AccountOut, Error])
def create_account(account: AccountIn, repo: AccountRepository = Depends()):
    return repo.create(account)


@router.get("/accounts", response_model=Union[Error, List[AccountOut]])
def get_all(repo: AccountRepository = Depends()):
    return repo.get_all()
