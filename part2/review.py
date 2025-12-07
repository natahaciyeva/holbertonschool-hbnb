from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review object.
    Relationships:
      - Review belongs to a User
      - Review belongs to a Place
    """
    def __init__(self, user_id, place_id, text, rating=0, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating  # Optional: validate 1–5

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text,
            "rating": self.rating
        })
        return base

