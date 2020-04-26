#The final code for the circle sine wave generator should look like this

r1=100
r2=10
t=0
circleList=[]

def setup():
    size(1000,1000)
    
def draw():
    global t, circleList
    background(200)
    #move to left-center of screen
    translate(width/2,height/2)
    noFill #don't color in the circle
    stroke(0) #black outline
    ellipse(0,0,2*r1,2*r1)
    
    #circling ellipse
    fill(255,0,0) #red
    x=r1*cos(t)
    y=r1*sin(t)     
    circleList=[y]+circleList[:245]
    
    ellipse(x,y,r2,r2)
    stroke(0,255,0)
    line(x,y,200,y)
    fill(255,0,0)
    ellipse(200,y,10,10)
    
    #loop over circleList to leave a trail:
    for i,c in enumerate(circleList):
        ellipse(200+i,c,5,5)
    t+=0.05
