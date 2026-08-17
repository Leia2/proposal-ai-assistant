from datetime import date, datetime, timezone
from pydantic import BaseModel, EmailStr

class StoredMeeting(BaseModel):
    meeting_id: str
    customer_email: EmailStr
    customer_name: str
    meeting_date: date
    summary: str
    business_name: str
    employee_email: EmailStr

    ingested_at: datetime
    processing_status: str