from abc import ABC, abstractmethod
from typing import Any, TypeVar, Optional


Command = TypeVar("Command")


class IMediator(ABC):
    
    @abstractmethod
    async def send(self, command: Command) -> Optional[Any]:
        raise NotImplementedError