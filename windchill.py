from fractions import *


def windchill():
    wchill = 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) + \
        ((0.4275 * T) * (V ** 0.16))
    return wchill


# change fahrenheit to celsius
def celsius():
    C = T * (Fraction(9, 5)) + 32
    wchill = 35.74 + (0.6215 * C) - (35.75 * (V ** 0.16)) + \
        ((0.4275 * C) * (V ** 0.16))
    return wchill


T = int(input('What is the temperature? '))
grades = str(input('Fahrenheit or Celsius (F/C)? '))
grades = grades.lower()


number = range(5, 61, 5)

for V in number:
    if grades == 'f':
        print(
            f'At temperature {T: .2f}F, and wind speed {V}mph, the windchill is: {windchill(): .2f}F')
    elif grades == 'c':
        print(
            f'At temperature {T: .2f}F, and wind speed {V}mph, the windchill is: {celsius(): .2f}F')
