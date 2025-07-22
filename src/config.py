from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    DATABASE_URL: str | None = "sqlite+aiosqlite:///./whether.db"

    URL_GET_COORDINATES: str = "https://geocoding-api.open-meteo.com/v1/search"
    URL_WHETHER_FORECAST: str = "https://api.open-meteo.com/v1/forecast"

    PROJECT_NAME: str = "Whether in the city"
    APP_VERSION: str = "1.0"

    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=('.env', '.env.prod')
    )


settings = Config()
