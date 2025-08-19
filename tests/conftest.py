import asyncio
from typing import Generator, AsyncGenerator

from motor.motor_asyncio import AsyncIOMotorClient
import pytest

from config import settings
from infrastructure.repository import MongoTaskRepository


@pytest.fixture(scope="module")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create event loop for all async tests."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    asyncio.set_event_loop(loop)
    
    yield loop
    
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.run_until_complete(loop.shutdown_default_executor())
    loop.close()
    asyncio.set_event_loop(None)

@pytest.fixture(scope="module")
async def mongo_db():
    client = AsyncIOMotorClient(settings.db_url)
    db = client[settings.db_name]
    yield db

@pytest.fixture(scope="module")
async def repository(mongo_db) -> AsyncGenerator[MongoTaskRepository, None]:
    repository = MongoTaskRepository(collection=mongo_db[settings.db_collection])
    yield repository
    await mongo_db.drop_collection(settings.db_collection)