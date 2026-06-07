from fastapi import Depends

from core.database import get_db
from repositories.book_repository import BookRepository
from services.book_service import BookService

def get_book_dependency(db=Depends(get_db)):
    return BookRepository(db)

def get_book_service(
    repository: BookRepository = Depends(get_book_dependency)
):
    return BookService(repository)