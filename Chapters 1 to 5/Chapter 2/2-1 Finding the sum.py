'''
Excersise 2-1: Finding the Sum
Find the sum of all the numbers from 1 to 100. How about 1 to 1000?

See a pattern?

'''
def mySum(num):
    running_sum=0
    for i in range(1,num+1):
        running_sum+=i
    return running_sum

print(mySum(100))
print(mySum(1000))
