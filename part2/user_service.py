from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, data: dict):
        required = ["email", "password"]
        for field in required:
            if field not in data:
                raise ValueError(f"{field} is required")

        user = User(
            email=data["email"],
            password=data["password"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", "")
        )
        return self.repo.create(user)

    def get_user(self, user_id: str):
        return self.repo.get_by_id(user_id)

    def list_users(self):
        return self.repo.list_all()

    def update_user(self, user_id: str, data: dict):
        user = self.repo.get_by_id(user_id)
        if not user:
            return None
        return self.repo.update(user, data)

