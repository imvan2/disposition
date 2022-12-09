from fastapi import FastAPI
from routers import questions, answers
# from fastapi.middleware.cors import CORSMiddleware
import os

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = [
#     os.environ.get("CORS_HOST", "http://localhost"),
#     "http://localhost:3000",
# ]
app = FastAPI(middleware=Middleware)

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(questions.router)
app.include_router(answers.router)
