from models.user import User

class UserRepository:
    def __init__(self):
        self.users = {}  # in-memory storage for now

    def create(self, user: User):
        self.users[user.id] = user
        return user

    def get_by_id(self, user_id: str):
        return self.users.get(user_id)

    def list_all(self):
        return list(self.users.values())

    def update(self, user: User, data: dict):
        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password = data["password"]  # Will NOT show in GET response
        user.save()
        return user

