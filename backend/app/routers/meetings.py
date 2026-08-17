from fastapi import APIRouter
from app.schemas.meeting import MeetingCreate
from app.services.meeting_service import MeetingService
from app.models.meeting import StoredMeeting

meeting_service = MeetingService()

router = APIRouter(
    prefix="/meetings",
    tags=["meetings"]
)

@router.post("")
def create_meeting(meeting: MeetingCreate) -> StoredMeeting: #the endpoint returns the schema type
    return meeting_service.create_meeting(meeting)




