import os
from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from queries.answers import AnswerIn, AnswerOut, AnswerRepo, Error
from typing import List, Optional, Union
from token_auth import get_current_user
print (os.getcwd())

router = APIRouter()

not_authorized = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
    headers={"WWW-Authenticate": "Bearer"},
)



@router.get("/answers", response_model=Union[List[AnswerOut], Error])
def get_all(
    repo: AnswerRepo = Depends(),
):
    return repo.get_all()


@router.post("/answers", response_model = AnswerOut)
def create_answer(
    answer:AnswerIn,
    repo: AnswerRepo = Depends(),
    ):
    return repo.create(answer)

@router.delete("/answers/{q_number}", response_model=bool)
def delete_answer(
    q_number: int,
    repo: AnswerRepo = Depends(),
) -> bool:
    return repo.delete(q_number)

@router.get("/answers/{q_number}", response_model=Optional[AnswerOut])
def get_one_answer(
  q_number: int,
  response: Response,
  repo: AnswerRepo = Depends(),
) -> AnswerOut:
  answer = repo.get_one(q_number)
  if answer is None:
    response.status_code = 404
  return answer


@router.put("/answers/{id}", response_model=Union[AnswerOut, Error])
def update_answer(
    id: int,
    answer: AnswerIn,
    repo: AnswerRepo = Depends(),
) -> Union[Error, AnswerOut]:
    return repo.update(id, answer)