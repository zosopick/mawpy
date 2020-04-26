#Drawing a circle of squares:

def setup():
    size(1000,1000)
    translate(width/2,height/2)
    for i in range(12):
        rect(200,0,50,50)
        rotate(radians(360/12))
