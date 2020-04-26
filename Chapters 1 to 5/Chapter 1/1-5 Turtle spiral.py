'''
Excersise 1-5: Turtle spiral

Make a funciton to draw 60 squares, turning 5 degrees after each
square and making each successive square bigger. Start at a length
of 5 and increment 5 units every square. 
'''

from turtle import *
shape('turtle')
speed(10)

length=5

def turtle_spiral():
     length=5
     for i in range(250):
          for j in range(4):
               forward(length)
               right(90)
          right(10)
          length+=5

turtle_spiral()
