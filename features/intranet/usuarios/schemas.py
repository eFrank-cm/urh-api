from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str # dni
    password: str
    