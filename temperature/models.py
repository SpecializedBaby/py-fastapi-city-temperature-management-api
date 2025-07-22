import datetime
from typing import Optional

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from city.models import City
from database import Base


class Temperature(Base):
    __tablename__ = "temperature_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    date_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    temperature: Mapped[str]
    city_id: Mapped[Optional[int]] = mapped_column(ForeignKey("city_table.id"))

    city: Mapped["City"] = relationship(bakc_related="temperatures")
