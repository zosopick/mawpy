'''
Excersise 1 2: A circle of squares

Write and run a function that draws 60 squares, turning 5 degrees
after each square. Use a loop! 

'''

from turtle import *
def square_looper():
     for j in range(60):
          
          for i in range(4):
               forward(100)
               right(90)
          right(5)

square_looper()

