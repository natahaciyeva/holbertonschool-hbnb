from app.extensions import db, bcrypt
from sqlalchemy import Column, String, Boolean
import uuid

class User(db.Model):
    __tablename__ = "users"

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(128), nullable=False, unique=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    password_hash = Column(String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Never expose password"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin
        }

