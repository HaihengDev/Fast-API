from pydantic import BaseModel, Field
from typing import Optional

class GameCreate(BaseModel):
    name: str = Field(max_length=40)
    imgUrl: str
    stock: int = Field(default=0)
    discount: int = Field(default=0)
    price: float | int= Field(gt=0)

class GameResponse(BaseModel):
    id: str
    name: str
    imgUrl: str
    stock: int
    discount: int
    price: float | int

class GameUpdate(BaseModel):
    name: Optional[str] = None
    imgUrl: Optional[str] = None
    stock: Optional[int] = None
    discount: Optional[int] = None
    price: Optional[float | int] = None