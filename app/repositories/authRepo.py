from sqlalchemy import select,or_
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.userModel import User
from app.models.refreshToken import RefreshToken

class AuthRepository:

    def __init__(self,db:AsyncSession) -> None:
        self.__db = db

    async def add_refresh_token(self,refresh_token:RefreshToken):
        try:
            self.__db.add(refresh_token)
            await self.__db.commit()
            await self.__db.refresh(refresh_token)
            return refresh_token
        except Exception as e:
            await self.__db.rollback()
            raise e
    
    async def add(self,user:User) -> User:
        try:
            self.__db.add(user)
            await self.__db.commit()
            await self.__db.refresh(user)
            return user
        except Exception as e:
            await self.__db.rollback()
            raise e

    async def get_user_with_identifier(
        self,
        identifier: str
    ) -> User | None:

        stmt = (
            select(User)
            .options(selectinload(User.refresh_tokens))
            .where(
                or_(
                    User.username == identifier,
                    User.email == identifier
                )
            )
        )

        response = await self.__db.execute(stmt)

        return response.scalar_one_or_none()
    