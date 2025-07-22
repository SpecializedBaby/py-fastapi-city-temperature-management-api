from pydantic import BaseModel, Field

from src.weatherapi.schemas.temperature import TemperatureRead


class CityBase(BaseModel):
    name: str = Field(..., frozen=True, max_length=128)
    additional_info: str


class CityCreate(CityBase):
    pass


class CityRead(CityBase):
    id: int
    temperatures: list[TemperatureRead] | None = None

    class Config:
        from_attributes = True
