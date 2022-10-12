from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urls.livros_router import router

api = FastAPI()
api.include_router(router, prefix="/livros")

origins = ['http://127.0.0.1:5500']

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)