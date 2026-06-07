from fastapi import Depends

from core.database import get_db
from repositories.product_repository import ProductRepository
from services.product_service import ProductService

def get_product_dependency(db=Depends(get_db)):
    return ProductRepository(db)

def get_product_service(
    repository: ProductRepository = Depends(get_product_dependency)
):
    return ProductService(repository)