'''

Exercise 5-2: Rainbow Triangles

Color each triangle of the rotating triangle sketch using stroke().

'''



def setup():
    size(1000,1000)
    rectMode(CENTER)
    strokeWeight(2)
    colorMode(HSB)
    
    
t=0

def draw():
    global t
    background(255)
    translate(width/2,height/2)
    
    for i in range(90):
       
        rotate(radians(360/90))
        pushMatrix()
        translate(200,0)
        stroke(2*i,255,255)

        rotate(radians(t+2*i*360/90))
        tri(100)
       
        popMatrix()
    t+=5

def tri(length):
    noFill()
    triangle(0,length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
