'''
Exercise 7-1: Draw a Julia set

Draw a Julia set with  c=0.285+0.01i
'''

#Writing the mandelbrot() function in Processing

from math import sqrt

#range of x-values
xmin=-2
xmax=2

#range of y-values
ymin=-2
ymax=2

#calculate the range
rangex=xmax-xmin
rangey=ymax-ymin

def setup():
    global xscl,yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl=float(rangex)/width
    yscl=float(rangey)/height
    
def draw():
    #origin in center
    translate(width/2,height/2)
    #go over all x's and y's on the grid
    x=xmin
    while x<xmax:
        y=ymin
        while y<ymin:
            z=[x,y]
            c=[-0.285,0.01]
            #put into the julia program
            col=julia(z,c,100)
            if col==100:
                fill(0)
            else:
                #map the color from 0 to 100
                #to 0 to 255
                #coll=map(coll,0,100,0,300)
                fill(3*coll,255,255)
            rect(x*xscl,y*yscl,1,1)
            y+=0.01
        x+=0.01
                
def julia(z,c,num): #returns the process num times and returs
                       #the divergence count
    count=0
    #define z1 as z
    z1=z
    #iterate num times
    while count<=num:
        #check for divergence
        if magnitude(z1)>2.0:
            #return the step it diverged on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),c)
        count+=1
    #if z hasn't diverged by the end
    return num

def cAdd(a,b):
     return [a[0]+b[0],a[1]+b[1]]


def cMult(u,v):
     return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
 
def magnitude(z):
     return sqrt(z[0]**2+z[1]**2)
