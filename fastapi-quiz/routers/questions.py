from fastapi import APIRouter, Depends
from queries.questions import QuestionIn, QuestionRepo, QuestionOut
router = APIRouter()

@router.post("/questions", response_model = QuestionOut)
def create_questions(
    question:QuestionIn,
    repo: QuestionRepo = Depends()
    ):
    print("question::::", question)
    print("repo::::",repo)

    return repo.create(question)
