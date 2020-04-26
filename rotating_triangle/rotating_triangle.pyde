
def setup():
    size(1000,1000)
    rectMode(CENTER)
    
t=0

def draw():
    global t
    translate(width/2,height/2)
    rotate(radians(t))
    triangle(0,0,100,100,300,-300)
    t+=0.5
