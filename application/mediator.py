from typing import Dict, Awaitable, Callable

from interfaces.mediator import IMediator, Command
from .exceptions import HandlerNotFoundError


class Mediator(IMediator):
    
    def __init__(self):
        self._handlers: Dict[type, Callable[[Command], Awaitable]] = {}
        
    def register_handler(self, command_type: type, handler: Callable[[Command], Awaitable]):
        self._handlers[command_type] = handler
        
    async def send(self, command: Command):
        handler = self._handlers.get(type(command))
        if not handler:
            raise HandlerNotFoundError(f'No handler found for command {type(command)}')
        return await handler(command)