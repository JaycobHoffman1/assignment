from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class User(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, nullable=False)
    password: Mapped[str] = mapped_column(db.String, nullable=False)
    role: Mapped[str] = mapped_column(db.String, nullable=False)
    roles: Mapped[List['Role']] = db.relationship(secondary='Roles')