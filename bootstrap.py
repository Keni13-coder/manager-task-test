from motor.motor_asyncio import AsyncIOMotorClient

from application.mediator import Mediator
from application.commands import CreateTask, DeleteTask, UpdateTask
from application.queries import GetListQuery, GetOneQuery
from application.handlers import create, get, get_list, update, delete
from infrastructure.repository import MongoTaskRepository
from config import settings

def bootstrap():
    mediator = Mediator()
    client = AsyncIOMotorClient(settings.db_url)
    db = client[settings.db_name]
    repository = MongoTaskRepository(collection=db[settings.db_collection])
    mediator.register_handler(CreateTask, lambda command: create(command, repository))
    mediator.register_handler(UpdateTask, lambda command: update(command, repository))
    mediator.register_handler(DeleteTask, lambda command: delete(command, repository))
    
    mediator.register_handler(GetListQuery, lambda query: get_list(query, repository))
    mediator.register_handler(GetOneQuery, lambda query: get(query, repository))
    return mediator