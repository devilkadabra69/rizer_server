from jose import jwt,JWTError,ExpiredSignatureError,exceptions
from datetime import datetime,timezone,timedelta
from app.core.config import get_settings,Settings

__config:Settings = get_settings()

class JwtService:

    ACCESS_TOKEN_SECRET:str = __config.ACCESS_TOKEN_SECRET
    REFRESH_TOKEN_SECRET:str = __config.REFRESH_TOKEN_SECRET
    ACCESS_TOKEN_EXPIRY_MIN:int = __config.ACCESS_TOKEN_EXPIRY_MIN
    REFRESH_TOKEN_EXPIRY_DAY:int = __config.REFRESH_TOKEN_EXPIRY_DAY
    ALGORITHM:str = __config.ALGORITHM

    @staticmethod
    def create_access_token(user_id:str) -> str:
        now = datetime.now(timezone.utc)
        payload = {
            "sub":str(user_id),
            "iat":now,
            "type":"accesss",
            "exp":now+timedelta(minutes=JwtService.ACCESS_TOKEN_EXPIRY_MIN)
        }
        return jwt.encode(claims=payload,key=JwtService.ACCESS_TOKEN_SECRET,algorithm=JwtService.ALGORITHM)
    
    @staticmethod
    def create_refresh_token(user_id:str) -> str:
        now = datetime.now(timezone.utc)
        payload = {
            "sub":str(user_id),
            "iat":now,
            "type":"refresh",
            "exp":now+timedelta(days=JwtService.REFRESH_TOKEN_EXPIRY_DAY)
        }
        return jwt.encode(claims=payload,key=JwtService.REFRESH_TOKEN_SECRET,algorithm=JwtService.ALGORITHM)
    
    @staticmethod
    def verify_access_token(token:str) -> dict:
        now = datetime.now(timezone.utc)
        try:
            payload = jwt.decode(token=token,key=JwtService.ACCESS_TOKEN_SECRET,algorithms=JwtService.ALGORITHM)
            if payload.get("type") == "refresh":
                raise exceptions.JWTClaimsError("The payload's type doesn't match!!")
            return payload
        except ExpiredSignatureError as ese:
            print(f"access token expired!!") #TODO:- I will change to logger
            raise ese
        except JWTError as jwe:
            print(f"Something  went wrong while decoding the token!!") #TODO:- I will change to logger
            raise jwe

    @staticmethod
    def verify_refresh_token(token:str) -> dict:
        now = datetime.now(timezone.utc)
        try:
            payload = jwt.decode(token=token,key=JwtService.REFRESH_TOKEN_SECRET,algorithms=JwtService.ALGORITHM)
            if payload.get("type") == "refresh":
                raise exceptions.JWTClaimsError("The payload's type doesn't match!!")
            return payload
        except ExpiredSignatureError as ese:
            print(f"access token expired!!") #TODO:- I will change to logger
            raise ese
        except JWTError as jwe:
            print(f"Something  went wrong while decoding the token!!") #TODO:- I will change to logger
            raise jwe