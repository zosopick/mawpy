def setup():
    size(2000,1000)
    
def draw():
    background(255)
    translate(500,500)
    level=int(map(mouseX,0,width,0,10))
    y(100,level)

def y(sz,level):
    if level>0:
        line(0,0,0,-sz)
        translate(0,-sz)
        angle=map(mouseY,0,height,0,180)
        rotate(radians(angle))
        y(0.8*sz,level-1)
        rotate(radians(-2*angle))
        y(0.8*sz,level-1)
        rotate(radians(angle))
        translate(0,sz)
