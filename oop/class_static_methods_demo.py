#!/usr/bin/env python3
"""
Class and Static Methods Demonstration
This module defines a Calculator class that demonstrates the use of
@classmethod and @staticmethod decorators.
"""

class Calculator:
    """A class demonstrating class and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Args:
            cls: The class itself (Calculator)
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b