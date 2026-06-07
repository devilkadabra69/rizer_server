from pydantic import BaseModel,EmailStr

class LoginPayload(BaseModel):

    identifier:str
    plain_password:str

class RegisterPayload(BaseModel):

    username:str
    email:EmailStr
    phone:str
    plain_password:str

