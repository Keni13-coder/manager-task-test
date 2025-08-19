from interfaces.task_repository import ITaskRepository

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError

class MongoTaskRepository(ITaskRepository):
    
    def __init__(self, collection: AsyncIOMotorClient):
        self._collection = collection

    async def get_list(self) -> list[dict]:
        return await self._collection.find().to_list()

    async def get(self, task_id: str) -> dict:
        return await self._collection.find_one({'task_id': task_id})

    async def create(self, task: dict) -> None:
        try:
            self._collection.insert_one(task)
        except PyMongoError:
            raise 

    async def update(self, task_id: str, owner_id: int, task: dict) -> None:
        try:
            self._collection.update_one({'task_id': task_id, 'owner_id': owner_id}, {'$set': task})
        except PyMongoError:
            raise

    async def delete(self, task_id: str, owner_id: int) -> None:
        try:
            self._collection.delete_one({'task_id': task_id, 'owner_id': owner_id})
        except PyMongoError:
            raise