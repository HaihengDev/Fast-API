from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from core.database import get_db
from schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)
from models.product import Product
from services.product import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get('/', response_model=list[ProductResponse])
async def get_products(db = Depends(get_db)):
    products = await ProductService.get_products(db)

    return [
        Product.to_dict(products)
        for product in products
    ]

@router.get('/{product_id}', response_model=ProductResponse)
async def get_product_by_id(
    product_id: str,
    db = Depends(get_db)
):
    product = await ProductService.get_product_by_id(db, product_id)

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
    product = await ProductService.create_product(db, payload.model_dump())

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
    product = await ProductService.update_product(
        db,
        product_id,
        payload.model_dump(exclude_unset=True)
    )

    return Product.to_dict(product)

@router.delete('/{product_id}')
async def delete_product(
    product_id: str,
    db=Depends(get_db)
):
    return await ProductService.delete_product(db, product_id)