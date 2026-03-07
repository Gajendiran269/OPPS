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
Encapsulation:
- Definition: Bundling data (attributes) and methods together, hiding internal details from the outside world
- Access Modifiers: Control visibility of class members
    - Public: Accessible from anywhere
    - Private: Accessible only within the class
    - Protected: Accessible within the class and by child classes
- Benefits: Data protection, controlled access, flexibility to change internal implementation
- Example:
    - Private attribute: `_bankBalance` (cannot be accessed directly from outside)
    - Public method: `deposit()`, `withdraw()` (controlled access to modify balance)
    - Getter/Setter: Methods to safely read and update private attributes
Polymorphisim
- Definition: The ability of objects to take multiple forms or for methods to have multiple implementations
- Types:
    - Compile-time Polymorphism (Static Binding):
        - Method Overloading: Multiple methods with same name but different parameters
        - Operator Overloading: Same operator behaves differently for different types
    - Runtime Polymorphism (Dynamic Binding):
        - Method Overriding: Child class provides different implementation of parent's method
        - Interface Implementation: Different classes implement same interface differently
- Benefits: Code flexibility, reusability, easier maintenance, extensibility
- Example:
    - Method Overloading: `print(int)`, `print(string)`, `print(double)`
    - Method Overriding: Parent class `Animal` has `makeSound()`, Child classes `Dog` and `Cat` override it differently
    - Runtime: `Animal dog = new Dog(); dog.makeSound();` calls Dog's version, not Animal's
Abstraction:
- Definition: Hiding complex implementation details and showing only the essential features to the user
- Purpose: Simplify complexity, reduce code redundancy, increase security
- How it works: Abstract classes and interfaces define what a class should do, not how to do it
- Abstract Class: 
    - Cannot be instantiated directly
    - Contain abstract methods (methods without implementation)
    - Child classes must implement abstract methods
    - Can have both abstract and concrete methods
- Interfaces:
    - Define a contract/blueprint for classes
    - All methods are abstract (in most languages)
    - Classes implement interfaces and provide implementations
- Benefits: Security, flexibility, maintainability, decoupling
- Example:
    - Abstract Class: `Vehicle` (abstract method: start(), stop())
    - Concrete Classes: `Car`, `Bike` implement start() and stop() differently
    - Interface: `PaymentMethod` (abstract method: pay())
    - Implementations: `CreditCard`, `PayPal` implement pay() in their own way