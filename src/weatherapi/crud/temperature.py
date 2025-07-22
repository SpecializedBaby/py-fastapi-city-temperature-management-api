from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.weatherapi.crud.city import get_city_list
from src.weatherapi.models.temperature import Temperature
from src.weatherapi.schemas.temperature import TemperatureCreate
from src.weatherapi.service import fetch_weather_from_api
async def update_temperature_in_cities(session: AsyncSession) -> dict:
    cities = await get_city_list(session=session)

    for city in cities:
        weather = await fetch_weather_from_api(city_name=city.name)

        temp_schema = TemperatureCreate(
            date_time=weather.date_time,
            temperature=weather.temperature,
            city_id=city.id
        )

        temp_obj = Temperature(**temp_schema.model_dump())

        session.add(temp_obj)

    await session.commit()
    return {"status": "updated", "count": len(cities)}
