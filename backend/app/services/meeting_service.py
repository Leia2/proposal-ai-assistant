from datetime import datetime, timezone

from app.models.meeting import StoredMeeting
from app.repositories.meeting_repository import MeetingRepository
from app.schemas.meeting import MeetingCreate


class MeetingService:
    def __init__(self) -> None:
        self.repository = MeetingRepository()

#self - represents the current instance of MeetingService
#meeting: MeetingCreate - means the service receives validated meeting data
#MeetingCreate - means it currently returns the same type
    def create_meeting(self, meeting: MeetingCreate) -> StoredMeeting:
        stored_meeting = StoredMeeting(
            **meeting.model_dump(),
            ingested_at=datetime.now(timezone.utc),
            processing_status ="pending"
        )

        self.repository.save(stored_meeting)
        return stored_meeting
    