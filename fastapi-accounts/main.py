from fastapi import FastAPI
from routers import accounts
from auth.authenticator import authenticator
# import os
# from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = [
#     os.environ.get("CORS_HOST", "http://localhost"),
#     "http://localhost:3000",
#     "https://moodz3.gitlab.io",
#     "https://accounts-microservice.onrender.com/token",
#     "https://accounts-microservice.onrender.com/api/signup/token",

# ]

origins = [
    "https://moodz3.gitlab.io",
    "http://localhost:3000",
    "http://localhost:8002",
    "http://localhost:8001/signup",
    "https://accounts-microservice.onrender.com/token",
    "https://accounts-microservice.onrender.com/api/signup/token",
]

# app = FastAPI()

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



app.include_router(accounts.router)
app.include_router(authenticator.router)
