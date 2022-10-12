from fastapi import FastAPI
from urls.livros_router import router

api = FastAPI()
api.include_router(router, prefix="/livros")