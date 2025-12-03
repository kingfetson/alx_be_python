class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        # Call the parent class constructor
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    # Method overriding - providing a specific implementation for Dog
    def make_sound(self):
        self.bark()
    
    def display_info(self):
        print(f"{self.name} is a {self.breed} dog.")

# Create an instance of Animal
print("=== Animal Instance ===")
generic_animal = Animal("Generic Animal")
generic_animal.eat()           # Inherited method
generic_animal.sleep()         # Inherited method
generic_animal.make_sound()    # Base class method
print()

# Create an instance of Dog
print("=== Dog Instance ===")
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.eat()           # Inherited from Animal
my_dog.sleep()         # Inherited from Animal
my_dog.bark()          # Dog-specific method
my_dog.make_sound()    # Overridden method (calls bark())
my_dog.display_info()  # Dog-specific method
print()

# Additional demonstration
print("=== Additional Demonstrations ===")

# Create another dog instance
another_dog = Dog("Rex", "German Shepherd")
another_dog.eat()
another_dog.bark()

# Show the inheritance hierarchy
print(f"\n=== Inheritance Information ===")
print(f"Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")
print(f"Is my_dog an instance of Dog? {isinstance(my_dog, Dog)}")
print(f"Is my_dog an instance of Animal? {isinstance(my_dog, Animal)}")

# Accessing attributes
print(f"\n=== Object Attributes ===")
print(f"Generic animal name: {generic_animal.name}")
print(f"My dog's name: {my_dog.name}")
print(f"My dog's breed: {my_dog.breed}")