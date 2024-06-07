from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    email: Mapped[str] = mapped_column("email", unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column("password", nullable=False)
