
def setup():
    size(1000,1000)
    rectMode(CENTER)
    colorMode(HSB)
    
    
def draw():
    background(255)
    for x in range(40):
        for y in range(40):
            d=dist(30*x,30*y,mouseX,mouseY)
            fill(0.5*d,255,255)
            rect(30*x,30*y,25,25)
