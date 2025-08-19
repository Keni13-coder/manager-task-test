from fastapi import APIRouter, HTTPException
from fastapi_cache.decorator import cache

from application.queries import GetListQuery, GetOneQuery
from application.commands import CreateTask, DeleteTask, UpdateTask
from .serializers import (
    RequestCreateTask,
    RequestDeleteTask,
    RequestUpdateTask,
    ResponseTaskId
    )

from .depends import DepMediator


router = APIRouter(prefix="/tasks")


@router.get("/")
@cache(expire=60)
async def get_all_tasks(mediator: DepMediator) -> list[dict]:
    return await mediator.send(GetListQuery())

@router.get("/{task_id}")
@cache(expire=60)
async def get_one_task(task_id: str, mediator: DepMediator) -> dict:
    return await mediator.send(GetOneQuery(task_id=task_id))

@router.post("/", description="Create a new task, returns task_id")
async def create_task(request: RequestCreateTask, mediator: DepMediator) -> ResponseTaskId:
    try:
        task_id = await mediator.send(CreateTask(**request.model_dump()))
        return {'task_id': task_id}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@router.patch("/")
async def update_task(request: RequestUpdateTask, mediator: DepMediator) -> ResponseTaskId:
    try:
        task_id = await mediator.send(UpdateTask(**request.model_dump()))
        return {'task_id': task_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@router.delete("/")
async def delete_task(request: RequestDeleteTask, mediator: DepMediator) -> ResponseTaskId:
    try:
        task_id = await mediator.send(DeleteTask(**request.model_dump()))
        return {'task_id': task_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        