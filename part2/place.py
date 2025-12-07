from models.base_model import BaseModel
from models.review import Review

class Place(BaseModel):
    """
    Place entity.
    Relationships:
      - Place has many Reviews
      - Place has many Amenities (many-to-many)
    """
    def __init__(self, owner_id, name, description="", price=0.0, **kwargs):
        super().__init__(**kwargs)
        self.owner_id = owner_id  # Relationship to User
        self.name = name
        self.description = description
        self.price = price
        self.reviews = []      # list of Review objects
        self.amenities = []    # list of Amenity objects

    def add_review(self, review: Review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "owner_id": self.owner_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "reviews": [r.id for r in self.reviews],
            "amenities": [a.id for a in self.amenities]
        })
        return base

