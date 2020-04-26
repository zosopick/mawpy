'''
Excersise 2-2: Finding the Average

Find the average of the list below:
d=[53,28,54,94,65,60,22,93,62,27,16,25,75,42,4,42,15,96,11,70,83,97,75]
'''

def averagerator(numList):
     s=sum(numList)
     l=len(numList)
     average=s/l
     print(average)
     

d=[53,28,54,94,65,60,22,93,62,27,16,25,75,42,4,42,15,96,11,70,83,97,75]

averagerator(d)
