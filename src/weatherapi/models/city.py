from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.weatherapi.models.base import Base


class City(Base):
    __tablename__ = "city_table"

    name: Mapped[str] = mapped_column(String(200), unique=True)
    additional_info: Mapped[str] = mapped_column(String, nullable=True)

    temperatures: Mapped[list["Temperature"]] = relationship("Temperature", back_populates="city")
