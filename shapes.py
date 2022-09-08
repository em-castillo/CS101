import math
# square
square = float(input("What is the length of a side of the square? "))
square_area = square * square
print("The area of the square is: " + str(square_area))
# print(f'The area of the square is: {square_area}')

# rectangle
rec_length = float(input("What is the length of the rectangle? "))
rec_width = float(input("What is the width of the rectangle? "))
rec_area = rec_length * rec_width
print("The area of the rectangle is: " + str(rec_area))

# circle
circle = float(input("What is the radius of the circle? "))
circle_area = (math.pi) * (circle**2)
rounded_area = '{:.2f}'.format(circle_area)  # 2 digits after
#rounded_area = round(circle_area,1)
print("The area of the circle is: " + str(rounded_area))
