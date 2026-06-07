from bson import ObjectId

class BookRepository:
    def __init__(self, db):
        self.collection = db.books

    async def get_all(self):
        books = []

        async for book in self.collection.find():
            books.append(book)
        return books

    async def get_by_id(self, book_id: str):
        return await self.collection.find_one(
            {"_id": ObjectId(book_id)}
        )

    async def create(self, data: dict):
        result = await self.collection.insert_one(data)

        return await self.collection.find_one(
            {"_id": result.inserted_id}
        )

    async def update(self, book_id: str, data: dict):
        return await self.collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": data}
        )

    async def delete(self, book_id: str):
        return await self.collection.delete_one(
            {"_id": ObjectId(book_id)}
        )