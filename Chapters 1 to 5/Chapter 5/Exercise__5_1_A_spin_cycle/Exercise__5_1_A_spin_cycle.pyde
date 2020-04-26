'''

Exercise 5-1: A spin cycle

Create a circle of equilateral triangles in a processing sketch and
rotate them using the rotate() function
'''

t=0

def setup():
    size(1000,1000)
    rectMode(CORNERS) #This keeps the squares rotating around the center
                      #also, one can use CORNER or CORNERS
    
def draw():
    global t
    background(255)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
       pushMatrix()
       translate(200,0)
       rotate(radians(5*t))#If we add this, the squares rotate faster
       tri(50)
       popMatrix()
       rotate(radians(360/12))
    t+=1
    
def tri(length):
        triangle(0,-length, -length*sqrt(3)/2, length/2, length*sqrt(3)/2, length/2)
