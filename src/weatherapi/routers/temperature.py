from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.weatherapi.crud.temperature import update_temperature_in_cities, get_list_temperature, get_temperatures_by_city_id
from src.weatherapi.schemas.temperature import TemperatureBase, TemperatureRead

temperature_router = APIRouter()


@temperature_router.post("/temperatures/update/")
async def update_weather_data_in_cities(session: AsyncSession = Depends(get_session)):
    return await update_temperature_in_cities(session=session)


@temperature_router.get("/temperatures/", response_model=list[TemperatureRead])
async def get_all_temperatures(session: AsyncSession = Depends(get_session), skip: int = 0, limit: int = 10):
    return await get_list_temperature(session=session, skip=skip, limit=limit)


@temperature_router.get("/temperatures/", response_model=list[TemperatureRead])
async def get_temperatures_by_city(city_id: int, session: AsyncSession = Depends(get_session)):
    return await get_temperatures_by_city_id(city_id=city_id, session=session)
