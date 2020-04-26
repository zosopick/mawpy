'''
Exercise 8-2: Enter the matrix

Solve this system of equations for w,x,y and z using the program you just wrote:

2*w-x+5*y+z=-3

3*w+2*x+2*y-6*z=-32

w+3*x+3*y-z=-47

5*w-2*x-3*y+3*z=49

'''
def gauss(A):
     m = len(A)
     n = len(A[0])

     for j,row in enumerate(A):
             #diagonal term to be 1
             #by dividing row by diagonal term
             if row[j] != 0: #diagonal entry can't be zero
                 divisor = row[j]
                 for i, term in enumerate(row):
                     row[i] = term / divisor
             #add the other rows to the additive inverse
             #for every row
             for i in range(m):
                 if i != j: #don't do it to row j
                     #calculate the additive inverse
                     addinv = -1*A[i][j]
                     #for every term in the ith row
                     for ind in range(n):
                         #add the corresponding term in the jth row
                         #multiplied by the additive inverse
                         #to the term in the ith row
                         A[i][ind] += addinv*A[j][ind]

     return A


matrix = [[2,-1,5,1,-3],   [3,2,2,-6,-32],     [1,3,3,-1,-47],     [5,-2,-3,3,49]]

print(gauss(matrix))
