from datetime import date
from pydantic import BaseModel, EmailStr


class MeetingCreate(BaseModel):
    meeting_id: str
    customer_email: EmailStr
    customer_name: str
    meeting_date: date
    summary: str
    business_name: str
    employee_email: EmailStr