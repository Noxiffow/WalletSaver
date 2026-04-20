from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TransactionBase(BaseModel):
    amount: float = Field(gt=0, description="Amount must be positive")
    description: Optional[str] = None
    type: str = Field(regex="^(income|expense)$", description="Type must be 'income' or 'expense'")
    date: datetime
    category_id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0, description="Amount must be positive")
    description: Optional[str] = None
    type: Optional[str] = Field(None, regex="^(income|expense)$", description="Type must be 'income' or 'expense'")
    date: Optional[datetime] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None


class TransactionResponse(TransactionBase):
    id: int
    is_active: bool
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True