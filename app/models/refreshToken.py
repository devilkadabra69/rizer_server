from app.models.baseModel import Base
from sqlalchemy import UUID as PG_UUID, String, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from uuid import uuid4, UUID

class RefreshToken(Base):

    __tablename__="refresh_tokens"
    id:Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),primary_key=True,default=uuid4)
    token:Mapped[str] = mapped_column(String,unique=True,nullable=True)
    replaced_by:Mapped[UUID|None] = mapped_column(PG_UUID(as_uuid=True),ForeignKey("refresh_tokens.id"),nullable=True)
    user_id:Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user:Mapped["User"] = relationship(back_populates="refresh_tokens") # type:ignore