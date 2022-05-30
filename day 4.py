input = ""
slot = None
with open('input.txt','r') as inp:
  for line in inp:
      input += line


input = input.split("\n\n")
sequence = input[0]
input = input[1:]
for i in range(len(input)):
  input[i] = input[i].split("\n")
  for j in range(len(input[i])):
    input[i][j] = input[i][j].split(" ")
    while "" in input[i][j]:  
      input[i][j].remove("")

def markNumber(num):
  for bingoBoard in input:
    for line in bingoBoard:
      for index in range(len(line)):
        if line[index] == num:
          line[index] = "x"

def checkWin(bingoBoard):
  for line in bingoBoard:
      flag = True
      for num in line:
        if num != "x":
          flag = False
          break
      if flag:
        return bingoBoard
  for row in range(len(bingoBoard)):
      flag = True
      for column in range(len(bingoBoard[row])):
        if bingoBoard[column][row] != "x":
          flag = False
          break
      if flag:
        return bingoBoard
  return False

def checkOneLoss(x):
  losses = 0
  s = None
  for i in input:
    if checkWin(i) == False:
      losses += 1
      input[0] = i
      if losses == 2:
         return False
  return True

def scoreBoard(bingoBoard,lastNumberCalled):
  ans = 0
  for line in bingoBoard:
    for num in line:
      if num != "x":
        #print(int(num))
        ans += int(num)
  print("ans", ans)
  return ans * int(lastNumberCalled)

sequence = sequence.split(",")
print("\n", sequence)
for i in sequence:
  markNumber(i)
  if checkOneLoss(i):
    print(i)
    print(input[0])
    print(scoreBoard(input[0],i))
    break

    


