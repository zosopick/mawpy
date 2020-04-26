def average(a,b):
     return (a+b)/2

def squareRoot(num,low,high):
     for i in range(20):
          guess=average(low,high)
          if guess**2==num:
               print(guess)
          elif guess**2>num:
               high=guess
          else:
               low=guess


     guess_2=guess**2
     if num>guess_2:
          value=guess_2/num
     else:
          value=guess_2/num
          

     print('The square root of {0} is {1}. The approximation is {2}% valid.'.format(num, guess, value))
    
if __name__=='__main__':
     num=int(input('Please enter whomstdve square root you wish to procure: '))
     low=1
     high=500
     squareRoot(num,low,high)


