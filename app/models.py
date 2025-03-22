from typing import Optional
from pydantic import BaseModel


class MsgPayload(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
