from typing import Optional
from sqlmodel import Field, SQLModel

class UserModel(SQLModel):
    user_name: str
    user_email:str
    user_password: str

class User(UserModel, table=True):
    user_id: Optional[int] = Field(None, primary_key=True)
    # user_name: str
    # user_email: str
    # user_password: str
    
    
class Token(SQLModel, table=True):
    token_id: Optional[int] = Field(None, primary_key=True)
    refresh_token: str