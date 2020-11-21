from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class DBModelMixin(BaseModel):
    ''' base class for all the data classes'''
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None