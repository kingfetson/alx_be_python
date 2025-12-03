class Person:
    def __init__(self, name, age):
        """Constructor to initialize Person attributes"""
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, {self.age} years old")
    
    def __del__(self):
        """Destructor to clean up and print farewell message"""
        print(f"Goodbye, {self.name}! The Person object has been destroyed.")
    
    def introduce(self):
        """Method to introduce the person"""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def have_birthday(self):
        """Method to increase age by 1"""
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")
    
    def update_name(self, new_name):
        """Method to update the person's name"""
        old_name = self.name
        self.name = new_name
        print(f"{old_name} has changed their name to {self.name}")

# Demonstrating constructor and destructor
def demonstrate_person_lifecycle():
    """Function to show the complete lifecycle of Person objects"""
    print("=== Person Lifecycle Demonstration ===\n")
    
    # Create Person objects (constructor is called)
    print("1. Creating Person objects:")
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    person3 = Person("Charlie", 35)
    
    print("\n2. Using Person objects:")
    person1.introduce()
    person2.introduce()
    person3.introduce()
    
    print("\n3. Modifying Person attributes:")
    person1.have_birthday()
    person2.update_name("Robert")
    person2.introduce()
    
    print("\n4. Demonstrating destructor with explicit deletion:")
    # Explicitly delete one object
    del person3
    print("Charlie's object has been explicitly deleted.")
    
    print("\n5. Creating a Person inside a function (local scope):")
    
    def create_local_person():
        """Function to create a Person object in local scope"""
        local_person = Person("David", 28)
        local_person.introduce()
        # local_person will be destroyed when function ends
    
    create_local_person()
    print("Function ended - David's object should be destroyed now.")
    
    print("\n6. Demonstrating scope-based destruction:")
    # person1 and person2 will be destroyed when function ends
    # or when we reassign them
    print("Reassigning person1 to a new object:")
    person1 = Person("Eve", 22)  # Original Alice object will be destroyed
    
    print("\n7. Setting person2 to None:")
    person2 = None  # Original Bob/Robert object will be destroyed
    
    print("\n8. Program ending - remaining objects will be destroyed:")

# Run the demonstration
demonstrate_person_lifecycle()

# Additional demonstrations outside function
print("\n=== Additional Demonstrations ===")

# Demonstrating with list of Person objects
print("\nCreating list of Person objects:")
people = [
    Person("Frank", 40),
    Person("Grace", 45),
    Person("Henry", 50)
]

print("\nAccessing people in list:")
for person in people:
    person.introduce()

print("\nRemoving people from list:")
people.pop()  # Henry will be destroyed
del people[0]  # Frank will be destroyed
people.clear()  # Grace will be destroyed
print("All people removed from list.")

print("\n=== End of Program ===")
# All remaining objects will be destroyed automatically