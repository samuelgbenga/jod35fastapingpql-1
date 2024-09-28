
from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    first_name: str =Field(max_length=25)
    last_name:  str =Field(max_length=25)
    middle_name: str = Field(max_length=25)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str  = Field(min_length=6)


class UserModel(BaseModel):
    uid: uuid.UUID 
    username: str
    first_name: str 
    last_name: str
    middle_name: str 
    is_verified: bool 
    email: str
    created_at: datetime

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str  = Field(min_length=6)

class LoginResponse(BaseModel):
    message: str
    auth_token: Optional[str] = None
    refresh_token: Optional[str] = None
    email: Optional[str] = None
    uid: Optional[str] = None
