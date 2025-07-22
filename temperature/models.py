import datetime
from typing import Optional

from sqlalchemy import func, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from city.models import City
from database import Base


class Temperature(Base):
    __tablename__ = "temperature_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    date_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    temperature: Mapped[float] = mapped_column(Float)
    city_id: Mapped[int] = mapped_column(ForeignKey("city_table.id"))

    city: Mapped["City"] = relationship(bakc_related="temperatures")
