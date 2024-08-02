from typing import Optional
from sqlmodel import Field, SQLModel

class Admin(SQLModel, table=True):
    admin_id: Optional[int] = Field(None, primary_key=True)
    admin_name: str
    admin_email: str
    admin_password: str
    
    