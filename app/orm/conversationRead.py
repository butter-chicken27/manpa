from sqlalchemy import Column, BigInteger, DateTime, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from orm.base import Base

class ConversationRead(Base):
    __tablename__ = "conversation_reads"

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    conversation_id = Column(BigInteger, ForeignKey("conversations.id"), nullable=False)
    last_read_at = Column(DateTime, server_default=func.sysdatetimeoffset())

    __table_args__ = (
        PrimaryKeyConstraint("user_id", "conversation_id", name="unique_conversation_read"),
    )

    user = relationship("User", back_populates="conversation_reads")
    conversation = relationship("Conversation", back_populates="reads")