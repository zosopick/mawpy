#Rotating around the center

t=0

def setup():
    size(1000,1000)
    rectMode(CENTER) #This keeps the squares rotating around the center
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
       rect(0,0,50,50)
       popMatrix()
       rotate(radians(360/12))
    t+=1
