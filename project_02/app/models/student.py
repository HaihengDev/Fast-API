from datetime import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class Student(Base):
  __tablename__ = 'students'

  id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True,
    index=True
  )

  name: Mapped[str] = mapped_column(
    String(40),
    nullable=False
  )

  age: Mapped[int] = mapped_column(
    Integer,
    nullable=False
  )

  score: Mapped[int] = mapped_column(
    Integer,
    nullable=False
  )

  created_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow
  )