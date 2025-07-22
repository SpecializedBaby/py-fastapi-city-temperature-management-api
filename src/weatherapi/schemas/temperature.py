import datetime

from pydantic import BaseModel, Field

from src.weatherapi.schemas.city import CityRead


class TemperatureBase(BaseModel):
    temperature: float = Field()


class TemperatureCreate(TemperatureBase):
    city_id: int


class TemperatureRead(TemperatureBase):
    id: int
    date_time: datetime.datetime
    city: CityRead

    class Config:
        from_attributes = True
