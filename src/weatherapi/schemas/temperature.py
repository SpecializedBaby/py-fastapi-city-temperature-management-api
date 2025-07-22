import datetime

from pydantic import BaseModel, Field

from src.weatherapi.schemas.city import CityBase


class TemperatureBase(BaseModel):
    temperature: float = Field()
    date_time: datetime.datetime | None = None


class TemperatureCreate(TemperatureBase):
    city_id: int


class TemperatureRead(TemperatureBase):
    id: int
    date_time: datetime.datetime
    city: CityBase

    class Config:
        from_attributes = True
