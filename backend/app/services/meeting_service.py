from datetime import datetime, timezone

from app.models.meeting import StoredMeeting
from app.schemas.meeting import MeetingCreate



class MeetingService:
#self - represents the current instance of MeetingService
#meeting: MeetingCreate - means the service receives validated meeting data
#MeetingCreate - means it currently returns the same type
    def create_meeting(self, meeting: MeetingCreate) -> StoredMeeting:
        return StoredMeeting(
            **meeting.model_dump(),
            ingested_at=datetime.now(timezone.utc),
            processing_status ="pending"
        )
    