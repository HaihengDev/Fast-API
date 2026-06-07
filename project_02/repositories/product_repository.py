from bson import ObjectId

class ProductRepository:
    def __init__(self, db):
        self.collection = db.products

    async def get_all(self):
        products = []

        async for product in self.collection.find():
            products.append(product)
        return products

    async def get_by_id(self, product_id: str):
        return await self.collection.find_one(
            {"_id": ObjectId(product_id)}
        )

    async def create(self, data: dict):
        result = await self.collection.insert_one(data)

        return await self.collection.find_one(
            {"_id": result.inserted_id}
        )

    async def update(self, product_id: str, data: dict):
        return await self.collection.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": data}
        )

    async def delete(self, product_id: str):
        return await self.collection.delete_one(
            {"_id": ObjectId(product_id)}
        )