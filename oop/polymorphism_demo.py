#!/usr/bin/env python3
"""
Polymorphism Demonstration
This module defines a Shape base class and Rectangle/Circle derived classes
that demonstrate polymorphism through method overriding.
"""

import math

class Shape:
    """Base class representing a geometric shape."""
    
    def area(self):
        """
        Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This method must be overridden in derived classes
        """
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length: float, width: float):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius: float):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area (π × radius²)
        """
        return math.pi * (self.radius ** 2)