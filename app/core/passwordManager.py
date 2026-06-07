from passlib.context import CryptContext

_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

class PasswordManager:

    @staticmethod
    def hash_password(plain_password:str) -> str:
        return _context.hash(secret=plain_password)
    
    @staticmethod
    def verify_password(plain_password:str, hash_password:str) -> bool:
        return _context.verify(secret=plain_password,hash=hash_password)
    