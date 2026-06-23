from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Basically import All

# database part
from app.database import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

#apis through controllers
from app.controller.user_controller import router as user_router
from app.controller.music_instrument_controller import router as music_router


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(music_router)

