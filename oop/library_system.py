#!/usr/bin/env python3
"""
Library System Implementation
This module defines a Book base class, EBook and PrintBook derived classes,
and a Library class that demonstrates composition.
"""

class Book:
    """Base class representing a book."""
    
    def __init__(self, title: str, author: str):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the ebook
            author (str): The author of the ebook
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self) -> str:
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical print book."""
    
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the print book
            author (str): The author of the print book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self) -> str:
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize a Library instance with an empty book list."""
        self.books = []
    
    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance
        """
        self.books.append(book)
        # No print statement here to match expected output
    
    def list_books(self) -> None:
        """List all books in the library with their details."""
        for book in self.books:
            print(book)
        # No extra formatting lines