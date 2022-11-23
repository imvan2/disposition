from fastapi import FastAPI
from routers import playlists


app = FastAPI()
app.include_router(playlists.router)
