class Bird:
    def __init__(self, name):
        """Initialize a Bird with a name"""
        self.name = name
        self.can_fly = True
    
    def fly(self):
        """Bird's flying behavior"""
        return f"{self.name} the bird is flying gracefully!"
    
    def chirp(self):
        """Bird-specific method"""
        return f"{self.name} says: Chirp chirp!"
    
    def __str__(self):
        return f"{self.name} (Bird)"

class Mammal:
    def __init__(self, name):
        """Initialize a Mammal with a name"""
        self.name = name
        self.has_fur = True
    
    def run(self):
        """Mammal's running behavior"""
        return f"{self.name} the mammal is running swiftly!"
    
    def growl(self):
        """Mammal-specific method"""
        return f"{self.name} says: Grrr!"
    
    def __str__(self):
        return f"{self.name} (Mammal)"

class Bat(Bird, Mammal):
    def __init__(self, name, wingspan):
        """Initialize a Bat with name and wingspan"""
        # Call both parent constructors explicitly to avoid MRO issues
        Bird.__init__(self, name)
        Mammal.__init__(self, name)
        self.wingspan = wingspan
        self.is_nocturnal = True
    
    def fly(self):
        """Override flying behavior for bat"""
        return f"{self.name} the bat is flying in the dark with {self.wingspan}cm wingspan!"
    
    def run(self):
        """Override running behavior for bat"""
        return f"{self.name} the bat is clumsily crawling on the ground!"
    
    def echolocate(self):
        """Bat-specific method"""
        return f"{self.name} is using echolocation: *click click*"
    
    def __str__(self):
        return f"{self.name} (Bat with {self.wingspan}cm wingspan)"

def demonstrate_multiple_inheritance():
    """Demonstrate multiple inheritance with Bat inheriting from Bird and Mammal"""
    
    print("=== Multiple Inheritance Demonstration ===\n")
    
    # Create instances of parent classes
    print("1. Creating parent class instances:")
    sparrow = Bird("Sparrow")
    lion = Mammal("Lion")
    
    print(f"Bird: {sparrow}")
    print(f"Fly: {sparrow.fly()}")
    print(f"Chirp: {sparrow.chirp()}")
    
    print(f"\nMammal: {lion}")
    print(f"Run: {lion.run()}")
    print(f"Growl: {lion.growl()}")
    
    print("\n" + "="*50 + "\n")
    
    # Create Bat instance
    print("2. Creating Bat instance (inherits from both Bird and Mammal):")
    bat = Bat("Dracula", 30)
    print(f"Bat: {bat}")
    print(f"Attributes:")
    print(f"  Name: {bat.name}")
    print(f"  Can fly: {bat.can_fly}")
    print(f"  Has fur: {bat.has_fur}")
    print(f"  Wingspan: {bat.wingspan}cm")
    print(f"  Is nocturnal: {bat.is_nocturnal}")
    
    print("\n" + "="*50 + "\n")
    
    # Demonstrate inherited and overridden methods
    print("3. Method demonstration:")
    print(f"Bat flying: {bat.fly()}")
    print(f"Bat running: {bat.run()}")
    print(f"Bat echolocation: {bat.echolocate()}")
    
    # Try calling parent class methods (if accessible)
    print(f"\nTrying to call parent methods:")
    print(f"Chirp (from Bird): {bat.chirp()}")
    print(f"Growl (from Mammal): {bat.growl()}")
    
    print("\n" + "="*50 + "\n")
    
    # Demonstrate Method Resolution Order (MRO)
    print("4. Method Resolution Order (MRO):")
    print(f"Bat MRO: {[cls.__name__ for cls in Bat.__mro__]}")
    print(f"Bird MRO: {[cls.__name__ for cls in Bird.__mro__]}")
    print(f"Mammal MRO: {[cls.__name__ for cls in Mammal.__mro__]}")
    
    print("\n" + "="*50 + "\n")
    
    # Type checking
    print("5. Type checking:")
    print(f"Is bat an instance of Bat? {isinstance(bat, Bat)}")
    print(f"Is bat an instance of Bird? {isinstance(bat, Bird)}")
    print(f"Is bat an instance of Mammal? {isinstance(bat, Mammal)}")
    print(f"Is Bat a subclass of Bird? {issubclass(Bat, Bird)}")
    print(f"Is Bat a subclass of Mammal? {issubclass(Bat, Mammal)}")
    
    print("\n" + "="*50 + "\n")
    
    # Fixed Diamond problem demonstration
    print("6. Diamond Problem Scenario (Fixed):")
    
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Animal.__init__ called for {name}")
        
        def make_sound(self):
            return f"{self.name} makes a sound"
    
    class WingedAnimal(Animal):
        def __init__(self, name, wingspan):
            super().__init__(name)  # Calls Animal.__init__
            self.wingspan = wingspan
            print(f"WingedAnimal.__init__ called for {name}")
        
        def make_sound(self):
            return super().make_sound() + " and flaps wings"
    
    class LandAnimal(Animal):
        def __init__(self, name, leg_count):
            super().__init__(name)  # Calls Animal.__init__
            self.leg_count = leg_count
            print(f"LandAnimal.__init__ called for {name}")
        
        def make_sound(self):
            return super().make_sound() + " and walks on land"
    
    class FlyingFox(WingedAnimal, LandAnimal):
        def __init__(self, name, wingspan, leg_count):
            # Call the __init__ of the first parent in MRO (WingedAnimal)
            super().__init__(name, wingspan)
            # Initialize LandAnimal attributes manually
            self.leg_count = leg_count
            print(f"FlyingFox.__init__ called for {name}")
        
        def make_sound(self):
            return f"{self.name} the flying fox screeches!"
    
    print("\nCreating FlyingFox (diamond inheritance):")
    flying_fox = FlyingFox("Fruit Bat", 150, 4)
    print(f"\nFlyingFox: {flying_fox.name}")
    print(f"Wingspan: {flying_fox.wingspan}cm")
    print(f"Leg count: {flying_fox.leg_count}")
    print(f"Sound: {flying_fox.make_sound()}")
    print(f"\nFlyingFox MRO: {[cls.__name__ for cls in FlyingFox.__mro__]}")
    
    print("\n" + "="*50 + "\n")
    
    # Practical usage examples
    print("7. Practical Usage Examples:")
    
    # Create different bats
    bats = [
        Bat("Batman", 40),
        Bat("Vampire", 25),
        Bat("Fruit Bat", 50)
    ]
    
    print("\nCollection of bats:")
    for b in bats:
        print(f"\n{b}")
        print(f"  {b.fly()}")
        print(f"  {b.run()}")
    
    # Simulating zoo animals
    print("\n\n8. Zoo Simulation:")
    
    class Zoo:
        def __init__(self):
            self.animals = []
        
        def add_animal(self, animal):
            self.animals.append(animal)
        
        def show_animals(self):
            for animal in self.animals:
                print(f"\n{animal}")
                if hasattr(animal, 'fly'):
                    print(f"  Flying: {animal.fly()}")
                if hasattr(animal, 'run'):
                    print(f"  Running: {animal.run()}")
    
    zoo = Zoo()
    zoo.add_animal(Bat("Nightwing", 35))
    zoo.add_animal(Bird("Robin"))
    zoo.add_animal(Mammal("Bear"))
    
    zoo.show_animals()

# Run the demonstration
demonstrate_multiple_inheritance()

# Additional examples
print("\n" + "="*50)
print("Additional Interactive Examples")
print("="*50)

# Create a bat and demonstrate method resolution
print("\n>>> my_bat = Bat('Shadow', 45)")
my_bat = Bat('Shadow', 45)

print("\n>>> print(my_bat)")
print(my_bat)

print("\n>>> print(my_bat.fly())")
print(my_bat.fly())

print("\n>>> print(my_bat.run())")
print(my_bat.run())

print("\n>>> print(my_bat.chirp())")
print(my_bat.chirp())

print("\n>>> print(my_bat.growl())")
print(my_bat.growl())

print("\n>>> print(my_bat.echolocate())")
print(my_bat.echolocate())

# Check attributes
print("\n>>> print(f'Name: {my_bat.name}')")
print(f'Name: {my_bat.name}')

print("\n>>> print(f'Can fly: {my_bat.can_fly}')")
print(f'Can fly: {my_bat.can_fly}')

print("\n>>> print(f'Has fur: {my_bat.has_fur}')")
print(f'Has fur: {my_bat.has_fur}')

print("\n>>> print(f'Is nocturnal: {my_bat.is_nocturnal}')")
print(f'Is nocturnal: {my_bat.is_nocturnal}')

# Demonstrate MRO explicitly
print("\n>>> print('Method Resolution Order:')")
print("Method Resolution Order:")

print("\n>>> for cls in Bat.__mro__:")
print("...     print(f'  {cls.__name__}')")
for cls in Bat.__mro__:
    print(f"  {cls.__name__}")

# Proper diamond problem example
print("\n" + "="*50)
print("Proper Diamond Problem Example")
print("="*50)

print("\n>>> class A:")
print("...     def __init__(self):")
print("...         print('A.__init__')")
class A:
    def __init__(self):
        print('A.__init__')
    
    def method(self):
        return 'A'

print("\n>>> class B(A):")
print("...     def __init__(self):")
print("...         print('B.__init__')")
print("...         super().__init__()")
class B(A):
    def __init__(self):
        print('B.__init__')
        super().__init__()
    
    def method(self):
        return 'B'

print("\n>>> class C(A):")
print("...     def __init__(self):")
print("...         print('C.__init__')")
print("...         super().__init__()")
class C(A):
    def __init__(self):
        print('C.__init__')
        super().__init__()
    
    def method(self):
        return 'C'

print("\n>>> class D(B, C):")
print("...     def __init__(self):")
print("...         print('D.__init__')")
print("...         super().__init__()")
class D(B, C):
    def __init__(self):
        print('D.__init__')
        super().__init__()
    
    def method(self):
        return super().method()

print("\n>>> print('\\nCreating D instance:')")
print('\nCreating D instance:')

print("\n>>> d = D()")
d = D()

print("\n>>> print(f'\\nD MRO: {[cls.__name__ for cls in D.__mro__]}')")
print(f'\nD MRO: {[cls.__name__ for cls in D.__mro__]}')

print("\n>>> print(f'D().method() returns: {d.method()}')")
print(f'D().method() returns: {d.method()}')