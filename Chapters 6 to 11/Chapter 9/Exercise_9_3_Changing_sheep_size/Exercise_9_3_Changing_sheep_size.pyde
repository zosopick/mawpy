'''
Exercise 9-3: Changing sheep size

Vary the size of the sheep according to their energy level.

'''


from random import choice

#Writing the class for sheep
 
WHITE=color(255)
BROWN=color(102,51,0)
RED=color(255,0,0)
GREEN=color(0,102,0)
YELLOW=color(255,255,0)
PURPLE=color(102,0,204)
colorList=[WHITE,RED,YELLOW,PURPLE]

class Sheep:
    def __init__(self,x,y,col):
        self.x=x #x-position
        self.y=y #y-position
        self.sz=size #size
        self.energy=20#energy level
        self.col=col
    
        
    def update(self):
        #make sheep walk randomly
        move=5
        if self.col==PURPLE:
            move=7
        self.energy-=1 #walking costs energy
        if self.energy<=0:
            sheepList.remove(self) #the sheep is gone after the energy is expended
        if self.energy>50:
            self.energy-=30 #giving birth takes energy
            #add another sheep to the list
            sheepList.append(Sheep(self.x,self.y,self.col))
        self.x+=random(-move,move)
        self.y+=random(-move,move)
        
        
        #wrap tha world Asteroids-Style
        if self.x>width:
            self.x%=width
        if self.y>height:
            self.y%=width
        if self.x<0:
            self.x+=width
        if self.y<0:
            self.y+=height
        #dind the patch of grass you're on in the grassList
        xscl=int(self.x/patchSize)
        yscl=int(self.y/patchSize)
        grass=grassList[xscl*rows_of_grass+yscl]
        if not grass.eaten:
            self.energy+=grass.energy
            grass.eaten=True
        fill(self.col) #it's own color
        ellipse(self.x,self.y,self.energy,self.energy)

class Grass:
    def __init__(self,x,y,sz):
        self.x=x
        self.y=y
        self.energy=4 #energy from eating this patch
        self.eaten=False #hasn't been eaten yet
        self.sz=sz
        
    def update(self):
        if self.eaten:
            if random(100)<=5:
                self.eaten=False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)

       
        
 #Now add more sheeps using the sheepList and updating the setup() and draw()
    
sheepList=[] #list to store sheep
grassList=[] #list to store grass 
patchSize=10 #size of each patch of grass

def setup():
    global rows_of_grass
    global patchSize
    rows_of_grass=height/patchSize
    size(1000,1000)
    noStroke()

    #create the sheep
    for i in range(20):
        sheepList.append(Sheep(random(width),random(height),choice(colorList)))
    
    #create the grass:
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
    
def draw():
    background(255)
    #update in grass first
    for grass in grassList:
        grass.update()
    #then for the sheep
    for sheep in sheepList:
        sheep.update()
