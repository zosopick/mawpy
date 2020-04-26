'''
Excersise 3-1: Finding the factor

The factors() function could come in handy for finding the greatest common factor (GCF) of two numbers.
Write a function that will return the GCF of two numbers.
'''

def gcf(a,b):
     factors1=[]
     factors2=[]

     for i in range(1,a+1):
          if a%i==0:
               factors1.append(i)
     for j in range(1,b+1):
          if b%j==0:
               factors2.append(j)

     result=set(factors1).intersection(factors2)
     print(max(result))
