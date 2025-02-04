from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    db_user: SecretStr
    db_address: SecretStr
    db_name: SecretStr
    
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8"
    )


config = Settings()