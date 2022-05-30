input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line.strip())
threeLargest = []
basinList = []

for x in range(len(input)):
  for y in range(len(input[x])):
    currentCell = input[x][y]
    flag = True
    if x != len(input) - 1:
      flag = flag and input[x + 1][y] > currentCell
    if x > 0:
      flag = flag and input[x - 1][y] > currentCell
    if y != len(input[x]) - 1:
      flag = flag and input[x][y + 1] > currentCell
    if y > 0:
      flag = flag and input[x][y - 1] > currentCell
    if flag:
      basinList.append({"x":x,"y":y})
      
def sizeOfBasin(x,y,checkedSet = set("a")):
  stringified = (str(x) + "," + str(y))
  if stringified in checkedSet:
    return 0
  checkedSet.add(stringified)
  ans = 0
  if x >= len(input) or x < 0 or y >= len(input[0]) or y < 0:
    return 0
  currentCell = input[x][y]
  if currentCell == "9":
    return ans
  ans += sizeOfBasin(x-1,y,checkedSet)
  ans += sizeOfBasin(x+1,y,checkedSet)
  ans += sizeOfBasin(x,y+1,checkedSet)
  ans += sizeOfBasin(x,y-1,checkedSet)
  return ans + 1

for i in basinList:
  threeLargest.append(sizeOfBasin(i["x"],i["y"]))
threeLargest.sort(reverse = True)
print(threeLargest[0] * threeLargest[1] * threeLargest[2])