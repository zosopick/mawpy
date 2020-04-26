#Writing the factors.py program

#Here are the factors involved:
    #1. Define the factors funciton, which takes a number as an argument
    #2. Create an empty factors list to fill with factors
    #3. Loop aover all the numbers from 1 to the given number
    #4. If any of the numbers divides evenly, add them to the list
    #5. Return the list of factors at the end
    

def factors(num):
     factorsList=[]
     for i in range(1,num+1):
          if num%i==0:
               factorsList.append(i)
     return  factorsList
