from pydantic import BaseModel, EmailStr, Field

class LoginUserDTO(BaseModel):
    email: EmailStr = Field(..., description="Valid email")
    password: str = Field(..., min_length=1, description="Password")
