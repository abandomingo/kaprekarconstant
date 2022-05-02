
newInt = '2145'
initialList = [None]*4

for x in range(len(newInt)): #newInt starts as a str
      temp = newInt[x] #split the characters into a list and turn them into intergers
      initialList[x] = temp

print(initialList)