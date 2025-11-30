%% HBnB High-Level Package Diagram

classDiagram
direction TB

package "Presentation Layer" {
    class API {
        <<Interface>>
        +UserService
        +PlaceService
        +ReviewService
        +AmenityService
    }
}

package "Business Logic Layer" {
    class Models {
        +User
        +Place
        +Review
        +Amenity
        +HBnBFacade
    }
}

package "Persistence Layer" {
    class Repositories {
        +UserRepository
        +PlaceRepository
        +ReviewRepository
        +AmenityRepository
        +DatabaseConnection
    }
}

API --> HBnBFacade : uses / calls
HBnBFacade --> Repositories : database operations

