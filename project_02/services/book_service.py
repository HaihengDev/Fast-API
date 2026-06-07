from bson import ObjectId
from fastapi import HTTPException

from repositories.book_repository import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def get_books(self):
        return await self.repository.get_all()

    async def get_book_by_id(self, book_id: str):
        if not ObjectId.is_valid(book_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )
        book = await self.repository.get_by_id(book_id)

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )
        return book

    async def create_book(self, data: dict):
        return await self.repository.create(data)

    async def update_book(self, book_id: str, update_data: dict):
        if not ObjectId.is_valid(book_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )
        result = await self.repository.update(book_id, update_data)

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )
        return await self.repository.get_by_id(book_id)

    async def delete_book(self, book_id: str):
        if not ObjectId.is_valid(book_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )
        result = await self.repository.delete(book_id)

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )
        return {
            "message": "Book deleted successfully!"
        }