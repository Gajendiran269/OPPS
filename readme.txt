Object Oriented Programming:
    - Software Develpoment Methodolgy which consists of class and Object
Principle:
    - Realistic Modelling
    - reusability
    - flexibility
    - Existing as different forms
Characteristics:
    - Abstraction  
    - Encapsulation
    - Inheritance
    - Polymorphisim

1.Object -> A Material thing which determined by its properties or attributes.It have state and behaviour

2.Class -> A **Class** is a blueprint or template for creating objects in object-oriented programming. 
It defines:
- **Properties (Attributes)**: Variables that hold data for each object
- **Methods (Functions)**: Actions or behaviors that objects can perform
- **Constructors**: Special methods used to initialize objects when they are created

**Example concept:**
- Class: `Car` (the blueprint)
- Object: A specific car instance (e.g., "my red Toyota") created from the Car class

Static vs Instance
    Variables:
        - Static Variable: Shared across all instances of a class, exists in memory only once
        - Instance Variable: Each object has its own copy, created when object is instantiated

    Methods:
        - Static Method: Called on the class itself, can only access static variables
        - Instance Method: Called on objects, can access both static and instance variables

    Example:
        - Static: `Car.totalCars` (count of all cars created)
        - Instance: `myCar.color` (specific to that car object)

Inheritance:
    - Definition: A mechanism where a child class inherits properties and methods from a parent class
    - Parent Class (Superclass): The class being inherited from
    - Child Class (Subclass): The class that inherits from the parent
    - Benefits: Code reuse, hierarchical relationships, easier maintenance
    - Types:
        - Single Inheritance: Child inherits from one parent class
        - Multiple Inheritance: Child inherits from multiple parent classes
        - Multilevel Inheritance: Child inherits from parent, which inherits from grandparent
        - Hierarchical Inheritance: Multiple children inherit from same parent
    - Example:
        - Parent Class: `Animal` (has properties: name, age; methods: eat(), sleep())
        - Child Class: `Dog` (inherits from Animal, adds: bark() method)