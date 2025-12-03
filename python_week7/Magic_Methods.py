class Book:
    def __init__(self, title, author, pages):
        """Initialize a Book object with title, author, and pages"""
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """User-friendly string representation"""
        return f"'{self.title}' by {self.author} ({self.pages} pages)"
    
    def __repr__(self):
        """Developer-friendly string representation for debugging"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Return the number of pages"""
        return self.pages
    
    def __eq__(self, other):
        """Check if two books are equal (same title and author)"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

# Demonstrate the Book class
def demonstrate_book_magic_methods():
    """Showcase the different magic methods of the Book class"""
    
    print("=== Creating Book Objects ===\n")
    
    # Create book instances
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = Book("1984", "George Orwell", 328)
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 310)  # Same as book1
    
    print("Book 1:", book1)
    print("Book 2:", book2)
    print("Book 3:", book3)
    
    print("\n=== Using str() and repr() ===\n")
    
    # Using str() - calls __str__
    print("Using str():")
    print("str(book1):", str(book1))
    print("str(book2):", str(book2))
    
    # Using repr() - calls __repr__
    print("\nUsing repr():")
    print("repr(book1):", repr(book1))
    print("repr(book2):", repr(book2))
    
    # Direct printing calls __str__
    print("\nDirect printing (calls __str__):")
    print(book1)
    print(book2)
    
    print("\n=== Using len() with Books ===\n")
    
    # Using len() - calls __len__
    print(f"Length of '{book1.title}': {len(book1)} pages")
    print(f"Length of '{book2.title}': {len(book2)} pages")
    
    print("\n=== Equality Comparison ===\n")
    
    # Using equality - calls __eq__
    print(f"Is book1 == book2? {book1 == book2}")
    print(f"Is book1 == book3? {book1 == book3}")
    print(f"Is book1 == 'The Hobbit'? {book1 == 'The Hobbit'}")
    
    print("\n=== Collections of Books ===\n")
    
    # Create a list of books
    books = [
        Book("Pride and Prejudice", "Jane Austen", 432),
        Book("To Kill a Mockingbird", "Harper Lee", 324),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
    ]
    
    print("List of books:")
    for book in books:
        print(f"  - {book}")
    
    print("\nList representation (using repr):")
    print(repr(books))
    
    print("\n=== Debugging with repr() ===\n")
    
    # Show how repr() is useful for debugging
    print("Creating a book for debugging:")
    debug_book = Book("Debug Book", "Debug Author", 999)
    print(f"Debug info: {debug_book!r}")  # Using !r format specifier
    print(f"Debug info (f-string with !r): {debug_book!r}")
    
    print("\n=== Recreating Objects from repr() ===\n")
    
    # Demonstrate how repr() can be used to recreate objects
    print("Original book:", book1)
    print("repr(book1):", repr(book1))
    
    # In real scenarios, eval() can recreate objects from repr() output
    # (Note: eval() should be used carefully with trusted input only)
    book1_repr = repr(book1)
    print("\nThe repr() output could be used with eval() to recreate the object")
    print(f"book1_repr = {book1_repr}")
    
    print("\n=== Summary ===\n")
    
    print("Key differences between __str__ and __repr__:")
    print("1. __str__: User-friendly, readable output")
    print("   Example:", str(book1))
    print("2. __repr__: Developer-friendly, unambiguous output")
    print("   Example:", repr(book1))
    print("   Ideally should allow object recreation with eval()")
    print("\nWhen each is called:")
    print("- print(obj) → __str__")
    print("- str(obj) → __str__")
    print("- repr(obj) → __repr__")
    print("- In containers like lists → __repr__")
    print("- In interactive shell → __repr__")

# Run the demonstration
demonstrate_book_magic_methods()

# Additional examples in interactive style
print("\n" + "="*50)
print("Additional Examples (Interactive Style)")
print("="*50)

# Simulating interactive Python session
print("\n>>> book = Book('Python Crash Course', 'Eric Matthes', 560)")
book = Book('Python Crash Course', 'Eric Matthes', 560)

print("\n>>> book  # In interactive Python, this calls __repr__")
print(f"Book('Python Crash Course', 'Eric Matthes', 560)")

print("\n>>> print(book)  # Explicit print calls __str__")
print("'Python Crash Course' by Eric Matthes (560 pages)")

print("\n>>> str(book)")
print("'Python Crash Course' by Eric Matthes (560 pages)")

print("\n>>> repr(book)")
print("Book('Python Crash Course', 'Eric Matthes', 560)")

print("\n>>> len(book)")
print("560")