#Using operators to write the average() function

'''
def average(a,b):
    value=(a+b)/2
    print(value)
    
if __name__=='__main__':
    a=float(input('Please enter the first number: '))
    b=float(input('Please enter the second number: '))

    average(a,b)
    '''

running_sum=0
for i in range(10):
    running_sum+=3

print(running_sum)
