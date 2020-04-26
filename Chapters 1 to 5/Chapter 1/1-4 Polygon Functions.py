'''
Excersise 1-4: Polygon Functions

Write a function called polygon that takes an integer as an
argumet and makes the turtle draw a polygon with that integers
number of sides

'''

from turtle import *
shape('turtle')

def polygon(n):
         for i in range(n):
              forward(100)
              right(360/n)
    
if __name__=='__main__':
    n=int(input('Please enter the number of sides: '))

    polygon(n)
