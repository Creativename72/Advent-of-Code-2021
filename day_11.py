flashes = [0]
tripFlag = [True]
input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line.strip())

class Octopus:
  def __init__(self,energyLevel,x,y):
    self.energyLevel = int(energyLevel)
    self.alreadyFlashed = False
    self.adjacent = []
    self.x = x
    self.y = y
    
  def linkAdjacent(self):
    self.linkSingle(self.x+1,self.y+1)
    self.linkSingle(self.x+1,self.y)
    self.linkSingle(self.x+1,self.y-1)
    self.linkSingle(self.x+0,self.y+1)
    self.linkSingle(self.x+0,self.y-1)
    self.linkSingle(self.x-1,self.y+1)
    self.linkSingle(self.x-1,self.y)
    self.linkSingle(self.x-1,self.y-1)

  def linkSingle(self,x,y):
    if x > -1 and x < len(input) and y > -1 and y < len(input):
      self.adjacent.append(octopiArray[x][y])

  def checkFlash(self):
    if self.energyLevel > 9 and not self.alreadyFlashed:
      self.flash()

  def flash(self):
    flashes[0] += 1
    self.energyLevel = 0
    self.alreadyFlashed = True
    for i in self.adjacent:
      if not i.alreadyFlashed:
        i.energyLevel += 1
        i.checkFlash()
  def __str__(self):
    return str(self.energyLevel)
  def __repr__(self):
    return self.__str__()

octopiArray = []
for x in range(len(input)):
  octopiArray.append([])
  for y in range(len(input[0])):
    octopiArray[x].append(Octopus(input[x][y], x, y))

def printStuff():
  for i in octopiArray:
    print(i)
  print("---------")

for i in octopiArray:
  for j in i:
    j.linkAdjacent()

for counter in range(10000):
  for i in octopiArray:
    for j in i:
      j.energyLevel += 1
  for i in octopiArray:
    for j in i:
      j.checkFlash()
  for i in octopiArray:
    for j in i:
      j.alreadyFlashed = False 
  if flashes[0] == len(octopiArray) * len(octopiArray[0]):
    print(counter + 1)
    break
  flashes[0] = 0