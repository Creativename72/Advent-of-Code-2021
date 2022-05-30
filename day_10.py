from collections import deque
input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line.strip())
openList = ["{","(","[","<"]
dictionary = {"}":"{",")":"(","]":"[",">":"<"}

scoreDict = {"(":1,"[":2,"{":3,"<":4}
delimiterStack = deque()

ans = 0
ansList = []
for line in input:
  delimiterStack = deque()
  flag = True
  for char in line:
    if char in openList:
      delimiterStack.append(char)
    elif delimiterStack.pop() != dictionary[char]:
      flag = False
      break;
  if flag == False:
    continue
  if delimiterStack:
    while delimiterStack:
      ans *= 5
      popped = delimiterStack.pop()
      ans += scoreDict[popped]
    ansList.append(ans)
    ans = 0
    
ansList.sort()
print(ansList)
print(ansList[(len(ansList)//2)])