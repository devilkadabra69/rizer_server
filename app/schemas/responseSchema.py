from typing import Any
from pydantic import BaseModel, Field

class MyResponse(BaseModel):
    status: str = "success"
    status_code: int = 200
    message: str = "success"
    data: Any = None
    errors: list[Any] = Field(default_factory=list)