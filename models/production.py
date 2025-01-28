from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Production(Base):
    __tablename__ = 'Production'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Products.id'), nullable=False)
    quantity_produced: Mapped[int] = mapped_column(db.Integer, nullable=False)
    date_produced: Mapped[str] = mapped_column(db.Date, nullable=False)