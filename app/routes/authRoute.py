from fastapi import APIRouter,Response,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.schemas.authSchema import LoginPayload,RegisterPayload
from app.schemas.responseSchema import MyResponse
from app.services.authService import AuthService

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/login",response_model=MyResponse)
async def login(response:Response,login_payload:LoginPayload,db:AsyncSession = Depends(get_db)):
    service = AuthService(db)
    res = await service.login_user(login_payload)

    response.set_cookie(
        "access_token",
        str(res.get("access_token")),
        samesite="lax",
        secure=False
        )
    response.set_cookie(
        "refresh_token",
        str(res.get("refresh_token")),
        samesite="lax",
        secure=False
        )
    
    return MyResponse(
        status_code=200,
        message="Logged in Successfully!",
        data=res
    )
    
@router.post("/register",response_model=MyResponse)
async def register(register_payload:RegisterPayload,db:AsyncSession = Depends(get_db)):
    service = AuthService(db)
    res = await service.register_user(register_payload)
    return MyResponse(
        status_code=201,
        message="Successfully Created the User",
        data=res
    )