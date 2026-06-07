from fastapi import APIRouter, Depends

from schemas.product_schema import (
    ProductCreate,
    ProductUpdate
)
from models.product_model import Product
from services.product_service import ProductService
from dependencies.product_dependency import (get_product_service)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get('/')
async def get_products(
    service: ProductService = Depends(get_product_service)
):
    products = await service.get_products()

    return [
        Product.to_dict(product)
        for product in products
    ]

@router.get('/{product_id}')
async def get_product_by_id(
    product_id: str,
    service: ProductService = Depends(get_product_service)
):
    product = await service.get_product_by_id(product_id)

    return Product.to_dict(product)

@router.post('/')
async def create_product(
    payload: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    product = await service.create_product(payload.model_dump())

    return Product.to_dict(product)

@router.put('/{product_id}',)
async def update_product(
    product_id: str,
    payload: ProductUpdate,
    service: ProductService = Depends(get_product_service)
):
    product = await service.update_product(
        product_id,
        payload.model_dump(exclude_unset=True)
    )

    return Product.to_dict(product)

@router.delete('/{product_id}')
async def delete_product(
    product_id: str,
    service: ProductService = Depends(get_product_service)
):
    return await service.delete_product(product_id)