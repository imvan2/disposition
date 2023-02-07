from fastapi import FastAPI
from routers import playlists, billboards2

# from routers import billboards

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

origins = [
    "https://moodz3.gitlab.io",
    "http://localhost:3000",
]

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

app.include_router(playlists.router)
app.include_router(billboards2.router)
# app.include_router(billboards.router)
