import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all HBnB models.
    Provides id, created_at, updated_at and common methods.
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id or str(uuid.uuid4())
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def save(self):
        """Updates the updated_at timestamp."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Converts the object into a dictionary for serialization."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

