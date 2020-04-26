'''
Exercise 9-1: Creating balls of different sizes

Give each ball it's own size, between 5 and 50 units

'''

ballList=[] #empty list to put the balls in

class Ball:
    def __init__(self,x,y):
        #How to initalize a ball
        self.xcor=x
        self.ycor=y
        self.xvel=random(-2,2)
        self.yvel=random(-2,2)
        self.xheight=random(5,50)
                    
        self.col=color(random(255),random(255),random(255))

    
    def update(self):
        self.xcor+=self.xvel
        self.ycor+=self.yvel
        #if the ball reaches a wall, switch direction
        if self.xcor>width or self.xcor<0:
            self.xvel=-self.xvel
        if self.ycor>height or self.ycor<0:
            self.yvel=-self.yvel
        fill(self.col)
    
        ellipse(self.xcor,self.ycor,self.xheight,self.xheight)
    
#We also need a setup  and we place 3 balls

def setup():
    size(1000,1000)
    for i in range(55):
        ballList.append(Ball(random(width),random(height)))
    
def draw():
    background(0) #black
    for ball in ballList:
        ball.update()
