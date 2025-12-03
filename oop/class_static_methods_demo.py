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
    def add(a: float, b: float) -> float:
        """
        Static method to add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method to multiply two numbers.
        
        Args:
            cls: The class itself (Calculator)
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b