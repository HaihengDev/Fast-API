from bson import ObjectId
from fastapi import HTTPException

class ProductService:

    @staticmethod
    async def get_products(db):
        products = []

        cursor = db.products.find()

        async for product in cursor:
            products.append(product)

        return products

    @staticmethod
    async def get_product_by_id(db, product_id: str):
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid product id"
            )
        product = await db.products.find_one({
            "_id": ObjectId(product_id)
        })

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        return product

    @staticmethod
    async def create_product(db, data: dict):
        result = await db.products.insert_one(data)

        product = await db.products.find_one(
            {"_id": result.inserted_id}
        )

        return product

    @staticmethod
    async def update_product(db, product_id: str, update_data: dict):
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid product id"
            )

        result = await db.products.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return await db.products.find_one({
            "_id": ObjectId(product_id)
        })

    @staticmethod
    async def delete_product(db, product_id: str):
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid product id"
            )

        result = await db.products.delete_one(
            {"_id": ObjectId(product_id)}
        )

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return {
            "message": "Product deleted"
        }