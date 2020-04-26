'''
Exercise 4-3: Finding more Roots


Using the graphing tool ypu just created  to find the roots
of 2*x**2+7*x-15=0

Check you answers using the quad() function
'''
'''
Processor code:
#Writing the grid() function
#Set the range of x-values
xmin=-50
xmax=50

#Set the range of y-values
ymin=-50
ymax=50

#Calculate the range
rangex=xmax-xmin
rangey=ymax-ymin


def setup():
    global xscl,yscl
    size(600,600)
    xscl=width/rangex
    yscl=-height/rangey

def draw():
    global xscl,yscl
    background(255) #White
    translate(width/2,height/2)
    grid(xscl,yscl)
    graphFunction()
    
def f(x):
'''
#return x**2; Now we change it to 6x^3+31x^2+3x-10

'''
    return 2*x**2+7*x-15

def graphFunction():
    x = xmin
    while x <= xmax:
        fill(0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
        
def grid(xscl, yscl):
     # Draws a grid for graphing
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0, xmax*xscl,
'''

#Quad code:
from math import sqrt
def quad(a,b,c):
     #Returns the solutions of an equation in the form of ax^2+bx+c
     x1=(-b+sqrt(b**2-4*a*c))/(2*a)
     x2=(-b-sqrt(b**2-4*a*c))/(2*a)
     print('The solutions are {0} and {1}.'.format(x1,x2))

quad(2,7,-15)
