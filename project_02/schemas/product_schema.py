from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    stock: int = Field(..., ge=0)
    price: float | int = Field(..., gt=0)

class ProductResponse(BaseModel):
    id: str
    name: str
    stock: int
    price: float | int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None
    price: Optional[float | int] = None