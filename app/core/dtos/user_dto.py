from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    id: str = ""
    username: str = ""
    email: EmailStr
