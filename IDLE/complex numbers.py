def cAdd(a,b):
     return [a[0]+b[0],a[1]+b[1]]


def cMult(u,v):
     return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]


from math import sqrt

def magnitude(z):
     return sqrt(z[0]**2+z[1]**2)
#Writing the mandelbrot() function in Processing

def mandelbrot(z,num): #returns the process num times and returs
                       #the divergence count
    count=0
    #define z1 as z
    z1=z
    #iterate num times
    while count<=num:
        #check for divergence
        if magnitude(z1)>2.0:
            #return the step it diverged on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    #if z hasn't diverged by the end
    return num
