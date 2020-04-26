     #The numberGame.py

from random import randint

def numberGame():
     number=randint(1,100)
     print("I'm thinking of a number between 1 and 100. Try to guess it.")
     guess=int(input("What's your guess? "))
     while guess:

          if number==guess:
                    print("That's correct! The number was indeed {0}".format(number))
          elif number>guess:
               print('Too low. Guess higher ')
          else:
               print('Too high. Guess lower')
          guess=int(input('Try again: '))

numberGame()
