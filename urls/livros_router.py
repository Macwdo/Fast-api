from fastapi import APIRouter
from controllers import livros_controllers as livros

router = APIRouter()

router.include_router(livros.router, prefix='/api')