from dataclasses import asdict
from uuid import uuid4

from loguru import logger

from .commands import CreateTask, DeleteTask, UpdateTask
from .queries import GetListQuery, GetOneQuery
from interfaces.task_repository import ITaskRepository

async def create(
    command: CreateTask,
    repository: ITaskRepository
):
    task_id = uuid4()
    payload = asdict(command)
    payload['task_id'] = str(task_id)
    try:
        await repository.create(payload)
        return task_id
    except Exception:
        logger.error('Failed to create task')
        raise
    
async def get(
    query: GetOneQuery,
    repository: ITaskRepository
    ):
    return await repository.get(query.task_id)

async def get_list(
    query: GetListQuery,
    repository: ITaskRepository
    ):
    return await repository.get_list()

async def update(
    command: UpdateTask,
    repository: ITaskRepository
    ):
    try:
        payload = {k:v for k,v in asdict(command).items() if v is not None}
        await repository.update(command.task_id, command.owner_id, payload)
        return command.task_id
    except Exception:
        logger.error('Failed to update task')
        raise

async def delete(
    command: DeleteTask,
    repository: ITaskRepository
    ):
    try:
        await repository.delete(command.task_id, command.owner_id)
        return command.task_id
    except Exception:
        logger.error('Failed to delete task')
        raise
    