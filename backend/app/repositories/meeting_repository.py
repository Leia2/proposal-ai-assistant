from google.cloud import firestore
from app.models.meeting import StoredMeeting


class MeetingRepository:
    def __init__(self) -> None:
        self.client = firestore.Client() #creating a firestore client
        self.collection = self.client.collection("meeting") #This gives us a reference to the Firestore collection

    def save(self, meeting: StoredMeeting) -> None:
        document = self.collection.document(meeting.meeting_id)
        document.set(meeting.model_dump())