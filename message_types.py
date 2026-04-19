from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class TaskMessage:
    request_id:str
    session_id:str
    task_type: str
    payload: Dict[str, Any]
    def to_dict(self)->Dict[str, Any]:
        return asdict(self)

@dataclass
class ResultMessage:
    request_id:str
    session_id:str
    status: str
    result: Dict[str, Any]
    def to_dict(self)->Dict[str, Any]:
        return asdict(self)
