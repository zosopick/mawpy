'''
Exercise 11-2: Changing the rule set

Change ruleset to the binary form of the number 90. What does the resulting CA look like?
'''

#Ca variables
w=2
rows=1000
cols=2000
ruleset=[0,1,0,1,1,0,1,0] #rule 90

def rules(a,b,c):
    return ruleset[7-(4*a+2*b+c)]

def setup():
    noStroke()
    global cells
    size(2000,1000)
    #first row:
    cells=[]
    for r in range(rows):
        cells.append([])
        for c in range(cols):
            cells[r].append(0)
    cells[0][cols//2]=1
    cells=generate()

def generate():
    for i, row in enumerate(cells):#look at first row
        for j in range(1,len(row)-1):
            left=row[j-1]
            me=row[j]
            right=row[j+1]
            if i<len(cells)-1:
                cells[i+1][j]=rules(left,me,right)
    return cells

def draw():
    background(255)
    #draw the CA
    for i, cell in enumerate(cells): #rows
        for j,v in enumerate(cell): #collumns
            if v==1:
                fill(0)
            else: fill(255)
            rect(j*w-(cols*w-width)/2,w*i,w,w)
