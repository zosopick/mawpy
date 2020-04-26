'''
Exercise 4-2: Fractions as coefficients

Use the equation() function to solve the last most sinister-looking equation

(1/2)x+(2/3)=(1/5)x+(7/8)

'''
def equation(a,b,c,d):
     a=float(a)
     b=float(b)
     c=float(c)
     d=float(d)
     solution=(d-b)/(a-c)
     print(' The solution is: {0}.'.format(solution))

equation(1/2,2/3,1/5,7/8)    
