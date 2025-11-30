classDiagram
class PresentationLayer {
    <<Package>>
    +API
    +Services
}

class BusinessLogicLayer {
    <<Package>>
    +Models (User, Place, Review, Amenity)
    +Facade
}

class PersistenceLayer {
    <<Package>>
    +Repositories
    +DatabaseAccess
}

PresentationLayer --> BusinessLogicLayer : uses Facade
BusinessLogicLayer --> PersistenceLayer : calls repositories

