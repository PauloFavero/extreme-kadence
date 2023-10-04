from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """User entity"""

    id: str
    email: EmailStr
    first_name: str
    last_name: str
