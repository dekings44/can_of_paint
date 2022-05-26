#Calculating the number of cans of paint needed to paint a given wall
import math

height = int(input('What is the height of the wall?\n'))
width = int(input('What is the width of the wall?\n'))

coverage = 5

def paint_can_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f'The number of cans required to paint a wall of {height} and {width} is {math.ceil(number_of_cans)}')


paint_can_calc(height=height, width=width, cover=coverage)