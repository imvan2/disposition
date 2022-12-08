from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    HTTPException,
    status,
)
from queries.accounts import (
    Account,
    AccountIn,
    AccountRepository,
    AccountOut,
    Error,
)
from typing import Union, List, Optional
from jwtdown_fastapi.authentication import Token
from pydantic import BaseModel
from auth.authenticator import authenticator


class AccountToken(Token):
    account: AccountOut


class AccountForm(BaseModel):
    username: str
    password: str


router = APIRouter()

not_authorized = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.get("/api/signup/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: dict = Depends(authenticator.get_current_account_data),
) -> AccountToken | None:

    # example of when you might want authenticator.try_get_current_account_data
    # if account:
    #     # logged in response
    # else:
    #     # non logged in response

    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


@router.post("/signup", response_model=Union[AccountToken, Error])
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    repo: AccountRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)

    account = repo.create(info, hashed_password)
    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.get("/accounts", response_model=Union[List[AccountOut], Error])
def get_all(repo: AccountRepository = Depends()):
    return repo.get_all()


@router.delete("/accounts/{id}", response_model=bool)
def del_account(
    id: int,
    repo: AccountRepository = Depends(),
) -> bool:
    return repo.delete(id)


@router.get("/accounts/{username}", response_model=Optional[Account])
def get_one_account(
    username: str,
    response: Response,
    repo: AccountRepository = Depends(),
) -> Account:
    account = repo.get_one(username)
    if account is None:
        response.status_code = 404
    return account


@router.put("/accounts/{id}", response_model=Union[AccountOut, Error])
def update_account(
    id: int,
    account: AccountIn,
    repo: AccountRepository = Depends(),
) -> Union[Error, AccountOut]:
    return repo.update(id, account)
