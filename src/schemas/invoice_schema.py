import pydantic as _pydantic
from typing import Optional
import datetime as _dt

class Invoice(_pydantic.BaseModel):
    
    invoice_id: int 
    to_customer: str
    suppliers_tin: str
    date_of_supply: _dt.datetime
    customer_tin: str
    date_of_invoice: _dt.datetime
    quantity_one: int
    description_one: str
    unit_price_one: float
    quantity_two: Optional[int] = 0
    description_two: Optional[str] = ""
    unit_price_two: Optional[float] = 0.0
    quantity_three: Optional[int] = 0
    description_three: Optional[str] = ""
    unit_price_three: Optional[float] = 0.0
    quantity_four: Optional[int] = 0
    description_four: Optional[str] = ""
    unit_price_four: Optional[float] = 0.0
    quantity_five: Optional[int] = 0
    description_five: Optional[str] = ""
    unit_price_five: Optional[float] = 0.0
    terms_of_payment: str
    
    class Config:
        orm_mode = True