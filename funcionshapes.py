import math


def compute_area_square():
    square_area = square * square
    return square_area


def compute_area_rectangle():
    rec_area = rec_length * rec_width
    return rec_area


def compute_area_circle():
    circle_area = (math.pi) * (circle**2)
    rounded_area = '{:.2f}'.format(circle_area)
    return rounded_area


# Write a new function called compute_area that accepts a first parameter
# of shape that can be either "square" or "circle" and then a value for
# the length of the side or the radius depending on the context. The
# function should then determine the correct function to use, based on
# the first parameter, call it, and return the value.
def compute_area(shape, value1, value2=0):
    area = -1

    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)

    return area


shape = ''
while shape != 'quit':
    shape = input('Which shape are you measuring? ')
    shape = shape.lower()
    if shape == 'square':
        square = float(input("What is the length of a side of the square? "))
        print(compute_area_square())
    elif shape == 'rectangle':
        rec_length = float(input("What is the length of the rectangle? "))
        rec_width = float(input("What is the width of the rectangle? "))
        print(compute_area_rectangle())
    elif shape == 'circle':
        circle = float(input("What is the radius of the circle? "))
        print(compute_area_circle())
