class Shape:
    def __init__(self, name):
        """Initialize a Shape with a name"""
        self.name = name
    
    def calculate_area(self):
        """Base method to calculate area - should be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement calculate_area()")
    
    def display_info(self):
        """Display information about the shape"""
        print(f"Shape: {self.name}")
    
    def __str__(self):
        """String representation of the shape"""
        return f"{self.name} (area calculation not implemented in base class)"

class Rectangle(Shape):
    def __init__(self, name, length, width):
        """Initialize a Rectangle with name, length, and width"""
        super().__init__(name)  # Call parent class constructor
        self.length = length
        self.width = width
    
    def calculate_area(self):
        """Override: Calculate area of rectangle (length × width)"""
        return self.length * self.width
    
    def display_info(self):
        """Override: Display rectangle-specific information"""
        super().display_info()  # Call parent method
        print(f"  Type: Rectangle")
        print(f"  Length: {self.length}")
        print(f"  Width: {self.width}")
        print(f"  Area: {self.calculate_area()}")
    
    def __str__(self):
        """String representation of rectangle"""
        return f"{self.name}: Rectangle with length={self.length}, width={self.width}, area={self.calculate_area()}"
    
    def is_square(self):
        """Check if the rectangle is actually a square"""
        return self.length == self.width

# Additional shape subclass for demonstration
class Circle(Shape):
    def __init__(self, name, radius):
        """Initialize a Circle with name and radius"""
        super().__init__(name)
        self.radius = radius
    
    def calculate_area(self):
        """Override: Calculate area of circle (π × radius²)"""
        import math
        return math.pi * self.radius ** 2
    
    def display_info(self):
        """Override: Display circle-specific information"""
        super().display_info()
        print(f"  Type: Circle")
        print(f"  Radius: {self.radius}")
        print(f"  Area: {self.calculate_area():.2f}")
    
    def __str__(self):
        """String representation of circle"""
        return f"{self.name}: Circle with radius={self.radius}, area={self.calculate_area():.2f}"

def demonstrate_shape_inheritance():
    """Demonstrate single inheritance with Shape and Rectangle classes"""
    
    print("=== Single Inheritance Demonstration ===\n")
    
    # Create base Shape object
    print("1. Creating a generic Shape:")
    generic_shape = Shape("Generic Shape")
    generic_shape.display_info()
    print(f"String representation: {generic_shape}")
    
    print("\n2. Trying to calculate area of generic Shape (should raise error):")
    try:
        area = generic_shape.calculate_area()
        print(f"Area: {area}")
    except NotImplementedError as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Create Rectangle objects
    print("3. Creating Rectangle objects:")
    rectangle1 = Rectangle("Rectangle 1", 5, 3)
    rectangle2 = Rectangle("Square 1", 4, 4)
    
    print("\nRectangle 1:")
    rectangle1.display_info()
    print(f"Is it a square? {rectangle1.is_square()}")
    
    print("\nRectangle 2:")
    rectangle2.display_info()
    print(f"Is it a square? {rectangle2.is_square()}")
    
    print("\n4. Calculating areas directly:")
    print(f"Area of {rectangle1.name}: {rectangle1.calculate_area()}")
    print(f"Area of {rectangle2.name}: {rectangle2.calculate_area()}")
    
    print("\n" + "="*50 + "\n")
    
    # Create Circle object (additional example)
    print("5. Creating a Circle object (additional subclass):")
    circle = Circle("My Circle", 7)
    circle.display_info()
    
    print("\n" + "="*50 + "\n")
    
    # Demonstrate polymorphism
    print("6. Demonstrating Polymorphism:")
    shapes = [
        Rectangle("Rect A", 8, 6),
        Rectangle("Square B", 5, 5),
        Circle("Circle C", 3),
        Rectangle("Rect D", 10, 4)
    ]
    
    print("\nList of shapes:")
    total_area = 0
    for shape in shapes:
        area = shape.calculate_area()  # Polymorphic call
        total_area += area
        print(f"  - {shape.name}: Area = {area:.2f}")
    
    print(f"\nTotal area of all shapes: {total_area:.2f}")
    
    print("\n" + "="*50 + "\n")
    
    # Demonstrate type checking and inheritance
    print("7. Type checking and inheritance:")
    print(f"Is rectangle1 an instance of Rectangle? {isinstance(rectangle1, Rectangle)}")
    print(f"Is rectangle1 an instance of Shape? {isinstance(rectangle1, Shape)}")
    print(f"Is rectangle1 an instance of Circle? {isinstance(rectangle1, Circle)}")
    print(f"Is Rectangle a subclass of Shape? {issubclass(Rectangle, Shape)}")
    print(f"Is Shape a subclass of Rectangle? {issubclass(Shape, Rectangle)}")
    
    print("\n" + "="*50 + "\n")
    
    # Demonstrate method overriding
    print("8. Method overriding demonstration:")
    print("\nCalling display_info() on different shapes:")
    for shape in shapes[:2]:  # Just first two for brevity
        print()
        shape.display_info()

# Run the demonstration
demonstrate_shape_inheritance()

# Additional interactive examples
print("\n" + "="*50)
print("Additional Interactive Examples")
print("="*50)

# Create more shape objects
print("\n>>> rect = Rectangle('My Rectangle', 12, 8)")
rect = Rectangle('My Rectangle', 12, 8)

print("\n>>> print(rect)")
print(rect)

print("\n>>> print(f'Area: {rect.calculate_area()}')")
print(f'Area: {rect.calculate_area()}')

print("\n>>> print(f'Is square? {rect.is_square()}')")
print(f'Is square? {rect.is_square()}')

# Using the shape as its base type
print("\n>>> shape_ref = rect  # Referring to rectangle as Shape")
shape_ref = rect

print("\n>>> print(f'Shape reference type: {type(shape_ref).__name__}')")
print(f'Shape reference type: {type(shape_ref).__name__}')

print("\n>>> print(f'Area through shape reference: {shape_ref.calculate_area()}')")
print(f'Area through shape reference: {shape_ref.calculate_area()}')

# Creating a square
print("\n>>> square = Rectangle('Perfect Square', 9, 9)")
square = Rectangle('Perfect Square', 9, 9)

print("\n>>> square.display_info()")
square.display_info()

print("\n>>> print(f'Perimeter (not implemented): 2 × (length + width) = {2 * (square.length + square.width)}')")
print(f'Perimeter (not implemented): 2 × (length + width) = {2 * (square.length + square.width)}')