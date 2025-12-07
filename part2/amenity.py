from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity object, can be associated with many Places.
    """
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "name": self.name
        })
        return base

