from datetime import date

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class BookCreate(BaseModel):
    title: str = Field(..., min_length=40),
    author: str = Field(..., min_length=40)
    release_date: date

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    release_date: date

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    release_date: Optional[date] = None