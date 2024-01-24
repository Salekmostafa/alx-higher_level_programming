#!/usr/bin/python3
"""Defines a Square class representing a geometric square."""


class Square:
    """Class Square: represents a square."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): The size of the square.
        """
        self.size = size  # Initialize size using the property setter

    @property
    def size(self):
        """int: Private size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  # Set the size of the square as a private attribute

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size**2

