from fastapi import APIRouter, Depends, Response, Request
from queries.questions import QuestionIn, QuestionRepo, QuestionOut, Error
from typing import List, Optional, Union

router = APIRouter()


@router.post("/questions", response_model=QuestionOut)
def create_questions(question: QuestionIn, repo: QuestionRepo = Depends()):
    print("question::::", question)
    print("repo::::", repo)

    return repo.create(question)


@router.get("/questions", response_model=Union[List[QuestionOut], Error])
def get_all(
    repo: QuestionRepo = Depends(),
):
    return repo.get_all()


@router.put("/questions/{id}", response_model=Union[QuestionOut, Error])
def update_question(
    id: int,
    question: QuestionIn,
    repo: QuestionRepo = Depends(),
) -> Union[Error, QuestionOut]:
    return repo.update(id, question)


@router.delete("/questions/{q_number}}", response_model=bool)
def delete_question(
    q_number: int,
    repo: QuestionRepo = Depends(),
) -> bool:
    return repo.delete(q_number)


@router.get("/questions/{q_number}", response_model=Optional[QuestionOut])
def get_one_question(
    q_number: int,
    response: Response,
    repo: QuestionRepo = Depends(),
) -> QuestionOut:
    question = repo.get_one(q_number)
    if question is None:
        response.status_code = 404
    return question
