from abc import ABC, abstractmethod


class ITaskRepository(ABC):
    
    @abstractmethod
    async def get_list(self):
        raise NotImplementedError

    @abstractmethod
    async def get(self, task_id: str):
        raise NotImplementedError

    @abstractmethod
    async def create(self, task: dict):
        raise NotImplementedError

    @abstractmethod
    async def update(self, task_id: str, owner_id: int, task: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, task_id: str, owner_id: int):
        raise NotImplementedError