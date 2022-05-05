
#kaprekar's constant
#this constant is 6174
#you take any 4 digit number with at least 2 different digits (leading 0 are allowed)
#arrange the digits in ascending order
#subtract the two numbers 
#and reapeat until u end up with 6174

#0111 = initial num
def kaprekar(initialNum, count):
    initialList = []

    for x in initialNum: #starts as a str
      temp = int(x) #split the characters into a list and turn them into intergers
      initialList.append(temp) #append each num in to a list [1,2,3,4]

    topNum = sorted(initialList, reverse=True) #[4,3,2,1]
    lowNum = sorted(initialList)               #[1,2,3,4]

    stringInt = [str(ints) for ints in topNum]
    tempString = "".join(stringInt)
    topInt = int(tempString)                    # turns the list into a single int  [4,3,2,1] -> 4321

    stringInt2 = [str(ints) for ints in lowNum] 
    tempString = "".join(stringInt2)  
    lowInt = int(tempString)                         # turns the list into a single int  [1,2,3,4] -> 1234
    
    if topInt <= 1000:                          #if the top integer is less than 1000 we need to add a trailing zero 999 -> 9990
      topInt *= 10                               #do this by muliply by 10
    
    initialNum = topInt - lowInt                 #subtract the two and make it our 'new' inital number
    count += 1                                  #up the count to know how many iterations it took

    print(f'{topInt} - {lowInt} = {initialNum}')  #format string to show math

    if initialNum == 6174:
      txt = "It took {0} iterations until you reached kaprekar's constant"
      print(txt.format(count))
    elif count > 50:
      print("The number may have been inputed wrong LOL ")
    else:
      kaprekar(str(initialNum),count)
      
      
if __name__ == '__main__':

  count = 0

  initialNum = input("Please enter a 4 digit number with at least 2 different digits:")
  kaprekar(initialNum,count)
