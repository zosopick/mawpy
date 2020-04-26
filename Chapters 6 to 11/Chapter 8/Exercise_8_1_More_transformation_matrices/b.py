'''
Exercise 8-1: More transformation matrices

See what happens to your shape when you change you transformation matrix to each
of the Pauli matrices:
    
a=[[1,0],[0,-1]] #Mirror flip along x axis
     b=[[0,-1],[-1,0]] #Mirror flip along x axis
c=[[-1,1],[1,1]]
'''

#Set the range of x-values
xmin=-10
xmax=10

#Range of y-values
ymin=-10
ymax=10

#Calculate the range
rangex=xmax-xmin
rangey=ymax-ymin

#Transformation matrix
transformation_matrix=[[0,-1],[-1,0]]

#Settigng up the stage
def setup():
    global xscl,yscl
    size(600,600)
    xscl=width/rangex
    yscl=-height/rangey
    noFill()

#Function which draws
def draw():
    global xscl,yscl
    background(255) #white
    translate(width/2,height/2) #move to center
    grid(xscl,yscl)
    strokeWeight(2)
    stroke(0)
    graphPoints(fmatrix)
    newmatrix=transpose(multmatrix(transformation_matrix,transpose(fmatrix)))
    stroke(255,0,0)#red resultant matrix
    graphPoints(newmatrix)

#Defining the shape
fmatrix=[[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]
 
    
#Multiplying matrices
def multmatrix(a,b):
     #Returns the product of matrix a and matrix b
     m = len(a) #number of rows in first matrix
     n = len(b[0]) #number of columns in second matrix
     newmatrix = []
     for i in range(m):
          row = []
          #for every column in b
          for j in range(n):
               sum1 = 0
               #for every element in the column
               for k in range(len(b)):
                    sum1+= a[i][k]*b[k][j]
               row.append(sum1)
          newmatrix.append(row)
     return newmatrix
 
#Transposing the matrix
def transpose(a):
    #Transposes the matrix a
    output=[]
    
    m=len(a)
    n=len(a[0])
    #create an n x m matrix 
    for i in range(n):
        output.append([])
        for j in range(m):
            #replace a[i][j] with a[j][i]
            output[i].append(a[j][i])
    return output

#Drawing the shape
def graphPoints(matrix):
    #raw line segments between consecutive points
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl,pt[1]*yscl)
    endShape(CLOSE)
    
#Drawing the Grid
def grid(xscl,yscl):
    #Draws a grid for graphing
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0)
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    




 
