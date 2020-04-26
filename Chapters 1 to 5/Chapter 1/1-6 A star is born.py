'''

Excersise 1-6: A star is born

First, write a 'star' function that will draw a five-pointed star.

Next, write a funciton called startSpiral() that will draw a spiral
of stars.
'''


from  turtle import *
shape('turtle')
speed(10)
'''
#This is the first part
def star():
     for i in range(5):
          forward(120)
          right(145)
star()
'''
#This is the second part
def starSpiral():
     length=5
     for i in range(40):
          for j in range(5):
               forward(length)
               right(145)
          right(10)
          length+=10

starSpiral()
     
