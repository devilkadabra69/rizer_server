from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.schemas.authSchema import RegisterPayload,LoginPayload
from app.schemas.userSchema import ResponseUser
from app.models.userModel import User
from app.models.refreshToken import RefreshToken
from app.repositories.authRepo import AuthRepository
from app.core.passwordManager import PasswordManager
from app.core.jwt import JwtService

class AuthService:

    def __init__(self,db:AsyncSession) -> None:
        self.__authRepo = AuthRepository(db=db)
        self.__passwordManager = PasswordManager
        self.__jwtService = JwtService

    async def register_user(self,register_payload:RegisterPayload):

        hashed_password = self.__passwordManager.hash_password(register_payload.plain_password)
        user_to_be_added = User(**register_payload.model_dump(exclude={"plain_password"}),hashed_password=hashed_password)
        await self.__authRepo.add(user=user_to_be_added)
        return ResponseUser.model_validate(user_to_be_added)
    
    async def login_user(self,login_payload:LoginPayload) -> dict:

        user_exists = await self.__authRepo.get_user_with_identifier(login_payload.identifier)
        if not user_exists:
            raise HTTPException(status_code=401,detail=f"User with identifier:- {login_payload.identifier} doesn't exists in our DB!")
        is_password_valid = self.__passwordManager.verify_password(login_payload.plain_password,user_exists.hashed_password)
        if not is_password_valid:
            raise HTTPException(status_code=401,detail=f"Wrong password entered!")
        access_token = self.__jwtService.create_access_token(str(user_exists.id))
        refresh_token = self.__jwtService.create_refresh_token(str(user_exists.id))
        user_exists.refresh_tokens.append(RefreshToken(token=refresh_token))
        await self.__authRepo.add(user_exists)
        return {
            "user":ResponseUser.model_validate(user_exists),
            "access_token":access_token,
            "refresh_token":refresh_token
        }