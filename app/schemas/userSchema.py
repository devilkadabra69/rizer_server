from pydantic import BaseModel,EmailStr,ConfigDict,field_validator
from uuid import UUID

class ResponseUser(BaseModel):

    id:str
    username:str
    email:EmailStr
    phone:str
    is_admin:bool

    model_config = ConfigDict(from_attributes=True)

    @field_validator("id", mode="before")
    @classmethod
    def convert_uuid_to_str(cls, value):
        if isinstance(value, UUID):
            return str(value)
        return value