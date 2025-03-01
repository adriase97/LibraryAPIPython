from pydantic import BaseModel, Field

class ReplaceClaimDTO(BaseModel):
    old_type: str = Field(..., min_length=1, description="Previous type of claim")
    old_value: str = Field(..., min_length=1, description="Previous value of the claim")
    new_type: str = Field(..., min_length=1, description="New type of claim")
    new_value: str = Field(..., min_length=1, description="New value of the claim")
