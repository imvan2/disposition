from fastapi import FastAPI
from routers import playlists, billboards2

# from routers import billboards


app = FastAPI()
app.include_router(playlists.router)
app.include_router(billboards2.router)
# app.include_router(billboards.router)
