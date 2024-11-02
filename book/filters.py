from ninja import FilterSchema, Field
from typing import Optional
from datetime import datetime

class BookFilterSchema(FilterSchema):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_date: Optional[datetime] = None
    price :  Optional[float] = None