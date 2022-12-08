from fastapi import FastAPI
from routers import playlists
# from routers import billboards


app = FastAPI()
app.include_router(playlists.router)
# app.include_router(billboards.router)
