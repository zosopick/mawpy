t=0

def setup():
    size(600,600)
    
def draw():
    global t
    background(255)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
        rect(200,0,50,50)
        rotate(radians(360/12))
    t+=1
    
