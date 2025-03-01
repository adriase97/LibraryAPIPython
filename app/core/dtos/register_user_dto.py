from pydantic import BaseModel, EmailStr, Field, validator

class RegisterUserDTO(BaseModel):
    username: str = Field(..., min_length=1, description="User name")
    email: EmailStr = Field(..., description="Valid email")
    password: str = Field(..., min_length=6, description="Password")
    confirm_password: str = Field(..., min_length=6, description="Password confirmation")

    @validator("confirm_password")
    def passwords_match(cls, confirm_password, values):
        if "password" in values and confirm_password != values["password"]:
            raise ValueError("Passwords do not match")
        return confirm_password
