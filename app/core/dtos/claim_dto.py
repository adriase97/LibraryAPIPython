from pydantic import BaseModel

class ClaimDTO(BaseModel):
    type: str
    value: str
