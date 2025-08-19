from dataclasses import dataclass


@dataclass(eq=False, kw_only=True)
class GetOneQuery:
    task_id: str
    
@dataclass(eq=False, kw_only=True)
class GetListQuery:
    pass