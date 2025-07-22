from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from temperature.models import Temperature


class City(Base):
    __tablename__ = "city_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True)
    additional_info: str | None = None

    temperatures: Mapped[list["Temperature"]] = relationship(back_populates="city")
