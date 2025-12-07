from models.base_model import BaseModel

class User(BaseModel):
    """
    User entity representing an application user.
    Relationships:
        - User can have many Reviews.
    """
    def __init__(self, email, password, first_name="", last_name="", **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password  # (Optional: hash this in persistence layer)
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []  # Holds Review objects

    def add_review(self, review):
        self.reviews.append(review)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "reviews": [review.id for review in self.reviews]
        })
        return base

