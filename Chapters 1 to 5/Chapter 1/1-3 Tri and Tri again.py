'''
Excersise 1-3: Tri and tri again

Write a triangle() function that will draw a triangle of 
a given "side length".
'''

from turtle import *
shape('turtle')

def triangle(sidelength):
    for i in range(3):
        forward(sidelength)
        right(120)
        
if __name__=='__main__':
    sidelength=float(input('Please enter the length of a side of a triangle: '))
    triangle(sidelength)
    
