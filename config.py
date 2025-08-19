from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    MODE: str
    
    DB_URL: str
    REDIS_URI: str
    DB_NAME: str
    DB_COLLECTION: Optional[str] = None
    
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
        

settings = Settings()