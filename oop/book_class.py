#!/usr/bin/env python3
"""
Book Class Implementation
This module defines a Book class that demonstrates various magic methods.
"""

class Book:
    """
    A class to represent a book with title, author, and publication year.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
    
    Magic Methods:
        __init__: Constructor to initialize book attributes
        __del__: Destructor that prints a deletion message
        __str__: User-friendly string representation
        __repr__: Developer-friendly string representation
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method.
        Prints a message when the Book instance is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the Book.
        
        Returns:
            str: String in format "title by author, published in year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Return an official string representation that can recreate the Book.
        
        Returns:
            str: String that looks like Book('title', 'author', year)
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"