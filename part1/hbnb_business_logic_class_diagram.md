classDiagram
direction TB

class BaseModel {
    +String id
    +Date created_at
    +Date updated_at
    +save() void
}

class User {
    +String first_name
    +String last_name
    +String email
    +String password
    +Boolean is_admin
    +updateProfile()
}

class Place {
    +String title
    +String description
    +Float price
    +Float latitude
    +Float longitude
    +updatePlace()
}

class Review {
    +Int rating
    +String comment
    +updateReview()
}

class Amenity {
    +String name
    +String description
    +updateAmenity()
}

%% Inheritance
User --|> BaseModel
Place --|> BaseModel
Review --|> BaseModel
Amenity --|> BaseModel

%% Associations
User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes

Place "1" --> "0..*" Review : has
Place "1" --> "0..*" Amenity : includes

