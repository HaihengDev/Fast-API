from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from core.database import get_db
from schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)
from models.product import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get('/', response_model=list[ProductResponse])
async def get_products(db = Depends(get_db)):
    products = []

    cursor = db.products.find()

    async for product in cursor:
        products.append(
            Product.to_dict(product)
        )
    return products

@router.get('/{product_id}', response_model=ProductResponse)
async def get_product_by_id(
    product_id: str,
    db = Depends(get_db)
):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(
            status_code=404,
            detail="Invalid product id"
        )
    product = await db.products.find_one(
        {"_id": ObjectId(product_id)}
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found!"
        )
    return Product.to_dict(product)

@router.post(
    '/',
    response_model=ProductCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_product(
    payload: ProductCreate,
    db = Depends(get_db)
):
    result = await db.products.insert_one(
        payload.model_dump()
    )

    product = await db.products.find_one(
        {"_id": result.inserted_id}
    )

    return Product.to_dict(product)

@router.put(
    '/{product_id}',
    response_model=ProductResponse
)
async def update_product(
    product_id: str,
    payload: ProductUpdate,
    db = Depends(get_db)
):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid product id"
        )

    update_data = payload.model_dump(
        exclude_unset=True
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

    updated = await db.products.find_one(
        {"_id": ObjectId(product_id)}
    )

    return Product.to_dict(updated)

@router.delete('/{product_id}')
async def delete_product(
    product_id: str,
    db=Depends(get_db)
):
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