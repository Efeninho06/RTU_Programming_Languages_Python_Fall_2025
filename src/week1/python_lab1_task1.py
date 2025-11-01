"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

# TODO: import math


def circle_area(radius):
    """Return the area of a circle given its radius."""
    # TODO: implement formula using math.pi


if __name__ == "__main__":
    # TODO: ask for user input, call circle_area(), and print formatted result

    import math


def circle_area(radius):
    """calculate area of circle with given radius"""
    area = math.pi * radius * radius
    return area


if __name__ == "__main__":
    # get user input for radius
    r = input("Enter radius: ")
    r = float(r)
    a = circle_area(r)
    print("Area of circle is:", round(a, 2))
