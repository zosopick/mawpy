'''
cellularAutomata.pyde
'''

GRID_W=100 #Grid width (x)
GRID_H=100 #Grid height (y)
generation=0 #starts from the 0th generation

class Cell: #defining a class of cells
    def __init__(self,c,r,state=0): #initial properties
        self.c=c
        self.r=r
        self.state=state
        
    def display(self): #what to show
        if self.state==1:
            fill(0) #black
        else:
            fill(255) #white
        rect (SZ*self.r,SZ*self.c,SZ,SZ)
        
    def checkNeighbors(self): #checking whether neighbors are alive
        if self.state==1:return 1 #on cell stay n
        neighbs=0
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            try:
                if cellList[self.r+dr][self.c+dc].state==1:
                    neighbs+=1
            except IndexError:
                continue
        if neighbs in [1,4]:
            return 1
        else:
            return 0
        

 
def setup(): #basic graphic setup
    global SZ, cellList
    size(600,600)
    SZ=width//GRID_W+1
    cellList=createCellList()
    
def draw(): #what to draw on the setup
    global generation, cellList
    cellList=update(cellList)
    for row in cellList:
        for cell in row:
            cell.display()
    generation+=1 #this updates the generation
    if generation==25: #Number of generations
        noLoop()
        
def update(cellList): #looping
    newList = []
    for r,row in enumerate(cellList):
        newList.append([])
        for c,cell in enumerate(row):
            newList[r].append(Cell(r,c,cell.checkNeighbors()))
    return newList[::]

            
def createCellList(): #Creating a list of cells from which to do the looping
    #crates a big list of off cells with one on cell in the center
    newList=[] #empty list for cells
    #populate the inital cell list
    for j in range(GRID_H):
        newList.append([]) #add empty row
        for i in range(GRID_W):
            newList[j].append(Cell(i,j,0)) #add off cells
        #center cell is set to on
    newList[GRID_H//2][GRID_W//2].state=1
    return newList


                


    
