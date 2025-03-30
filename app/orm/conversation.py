from sqlalchemy import Column, BigInteger, DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from orm.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    client_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    expert_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    last_message_at = Column(DateTime, server_default=func.sysdatetimeoffset())
    created_at = Column(DateTime, server_default=func.sysdatetimeoffset())

    __table_args__ = (
        UniqueConstraint("client_id", "expert_id", name="unique_conversation"),
    )

    client = relationship("User", foreign_keys=[client_id], back_populates="client_conversations")
    expert = relationship("User", foreign_keys=[expert_id], back_populates="expert_conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")
    reads = relationship("ConversationRead", back_populates="conversation", cascade="all, delete-orphan")