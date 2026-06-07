from bson import ObjectId
from fastapi import HTTPException

from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_products(self):
        return await self.repository.get_all()

    async def get_product_by_id(self, product_id: str):
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid product id"
            )
        product = await self.repository.get_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        return product

    async def create_product(self, data: dict):
        return await self.repository.create(data)

    async def update_product(self, product_id: str, update_data: dict):
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid product id"
            )
        result = await self.repository.update(product_id, update_data)

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
        return await self.repository.get_by_id(product_id)

    async def delete_product(self, product_id: str):
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid product id"
            )
        result = await self.repository.delete(product_id)

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return {
            "message": "Product deleted"
        }