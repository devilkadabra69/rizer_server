from sqlalchemy import String,Boolean,DateTime,UUID as PG_UUID,or_,select,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.models.baseModel import Base
from uuid import uuid4,UUID

class User(Base):

    __tablename__="users"
    id:Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),primary_key=True,default=uuid4)
    username:Mapped[str] = mapped_column(String(length=12),unique=True,index=True,nullable=False)
    email:Mapped[str] = mapped_column(String,unique=True,index=True,nullable=False)
    phone:Mapped[str] = mapped_column(String,unique=True,nullable=False)
    hashed_password:Mapped[str] = mapped_column(String,nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    refresh_tokens:Mapped[list["RefreshToken"]] = relationship(back_populates="user",cascade="all, delete-orphan") # type:ignore
    