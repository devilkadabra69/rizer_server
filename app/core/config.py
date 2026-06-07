from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class ServerConfig(BaseSettings):

    SERVER_VERSION:str
    SERVER_BASE_PATH:str
    SERVER_BASE_NAME:str
    SERVER_HOST:str
    SERVER_PORT:int

class JwtConfig(BaseSettings):

    ACCESS_TOKEN_SECRET:str
    REFRESH_TOKEN_SECRET:str
    ACCESS_TOKEN_EXPIRY_MIN:int
    REFRESH_TOKEN_EXPIRY_DAY:int
    ALGORITHM:str

class DBConfig(BaseSettings):

    DB_USERNAME:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_HOST:str
    DB_PORT:int
    DB_TYPE_NAME:str
    DB_DRIVER_NAME:str

    @property
    def construct_db_url(self):
        return f"""{self.DB_TYPE_NAME}+{self.DB_DRIVER_NAME}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"""

class Settings(ServerConfig,JwtConfig,DBConfig):
   
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings() #type: ignore
