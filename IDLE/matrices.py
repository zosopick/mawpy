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
