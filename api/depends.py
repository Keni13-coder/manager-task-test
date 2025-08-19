from typing import Annotated

from fastapi import Depends

from bootstrap import bootstrap
from interfaces.mediator import IMediator


class SingleMediator:
    def __init__(self):
        self._mediator = bootstrap()
    
    def __call__(self):
        return self._mediator
    
    @property
    def mediator(self):
        return self._mediator

singl_mediator = SingleMediator()

DepMediator = Annotated[IMediator, Depends(singl_mediator)]