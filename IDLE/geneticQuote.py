#geneticQuote.py


import random

target='I never go back on my word, because that is my Ninja way.' #We try go guess this
characters=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,'?!"#Using these symbols

def makeList():
    #Returns a list of characters with the same length as the target
    charList=[] #empty list to fill with random characters
    for i in range(len(target)):
        charList.append(random.choice(characters))
    return charList

def score(mylist):
    #Returns on integer: the number of matches with target
    matches=0
    for i in range(len(target)):
        if mylist[i]==target[i]:
            matches+=1
    return matches

def mutate(mylist):
    #Return mylist with one letter changed
    newlist=list(mylist)
    new_letter=random.choice(characters) #randomly selects a new letter
    index=random.randint(0,len(target)-1) #randomly seletes a new location 
    newlist[index]=new_letter
    return newlist


random.seed()
bestList=makeList()
bestScore=score(bestList)

    #We need to keep track of how many scores were made
    
guesses=0
while True:  #infinite loop for mutating the bestList and scoring it
    guess=mutate(bestList)
    guessScore=score(guess)
    guesses+=1
    
    if guessScore<=bestScore: #if the score is lower than the best one, go to the next iteration
        continue
        
    print(''.join(guess),guessScore,guesses) #if the score is optimal print the solution and stop loop
    if guessScore==len(target):
        break
        
    bestList=list(guess) #otherwise, set bestList and bestScore for the values right now
    bestScore=guessScore
