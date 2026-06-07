from fastapi import APIRouter, Depends, status

from schemas.book_schema import (
    BookCreate,
    BookUpdate
)
from models.book_model import Book
from services.book_service import BookService
from dependencies.book_dependency import (get_book_service)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get('/')
async def get_products(
    service: BookService = Depends(get_book_service)
):
    books = await service.get_books()

    return [
        Book.to_dict(book)
        for book in books
    ]

@router.get('/{book_id}')
async def get_book_by_id(
    book_id: str,
    service: BookService = Depends(get_book_service)
):
    book = await service.get_book_by_id(book_id)
    return Book.to_dict(book)

@router.post('/')
async def create_book(
    payload: BookCreate,
    service: BookService = Depends(get_book_service)
):
    book = await service.create_book(payload.model_dump())
    return Book.to_dict(book)

@router.put('/{book_id}')
async def update_book(
    payload: BookUpdate,
    book_id: str,
    service: BookService = Depends(get_book_service)
):
    book = await service.update_book(
        book_id,
        payload.model_dump(
            exclude_unset=True
        )
    )
    return Book.to_dict(book)

@router.delete('/{book_id}')
async def delete_book(
    book_id: str,
        service: BookService = Depends(get_book_service)
):
    return await service.delete_book(book_id)