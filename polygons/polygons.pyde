#Drawing an equiliteral triangle with loops

def setup():
    size(1000,1000)
    
def draw():
    translate(width/2,height/2)
    polygon(3,200)#3 sides, 200 units from center
    
def polygon(sides,distance):
    beginShape()
    for i in range(sides):
        step=radians(360/sides)
        vertex(distance*cos(i*step),distance*sin(i*step))
    endShape(CLOSE)
