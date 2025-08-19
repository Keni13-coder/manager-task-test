from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger
import sys, os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    MODE: str
    
    DB_URL: str
    REDIS_URI: str
    DB_NAME: str
    DB_COLLECTION: Optional[str] = None
    ALLOWED_HOSTS: list[str] = ['localhost:3000']
    
    @property
    def redis_uri(self) -> str:
        return self.REDIS_URI
    
    @property
    def db_url(self) -> str:
        return self.DB_URL
        
    @property
    def db_name(self) -> str:
        if self.MODE == 'test':
            return f'{self.DB_NAME}_test'
        return self.DB_NAME
        
    @property
    def db_collection(self) -> Optional[str]:
        if self.DB_COLLECTION:
            return self.DB_COLLECTION

def init_logger():     
    logger.add(
        sink=sys.stdout,
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
        )
        
    logger.add(
        sink=os.path.join("logs", "app_{time:YYYY-MM-DD}.log"),
        rotation="1 day",
        retention="7 days",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
    )

    logger.add(
        sink=os.path.join("logs", "errors_{time:YYYY-MM-DD}.log"),
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
        rotation="1 day"
    )
    
settings = Settings()
init_logger()