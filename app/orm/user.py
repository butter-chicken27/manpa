from sqlalchemy import Column, BigInteger, String, DateTime, CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from orm.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    role = Column(String(10), nullable=False)
    created_at = Column(DateTime, server_default=func.sysdatetimeoffset())

    __table_args__ = (
        CheckConstraint(role.in_(["client", "expert"]), name="check_role_valid"),
    )

    client_conversations = relationship("Conversation", foreign_keys="Conversation.client_id", back_populates="client")
    expert_conversations = relationship("Conversation", foreign_keys="Conversation.expert_id", back_populates="expert")
    messages = relationship("Message", back_populates="sender")
    conversation_reads = relationship("ConversationRead", back_populates="user")