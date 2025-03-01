from pydantic import BaseModel, Field, validator

class ChangePasswordUserDTO(BaseModel):
    current_password: str = Field(..., min_length=1, description="Current password")
    new_password: str = Field(..., min_length=1, description="New password")

    @validator("new_password")
    def passwords_must_not_match(cls, new_password, values):
        if "current_password" in values and new_password == values["current_password"]:
            raise ValueError("The new password cannot be the same as the current one")
        return new_password
