import sys
sys.setrecursionlimit(30)
input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line.strip().split("-"))

class Cave:
  def __init__(self, name):
    self.bigCave = name.isupper()
    self.passes = 0
    self.name = name
    self.paths = []
  def __str__(self):
    return self.name
  def __repr__(self):
    return self.__str__()

caveNames = set()

for i in input:
  for j in i:
    if j not in caveNames:
      caveNames.add(j)

caveDict = {}

for i in caveNames:
  caveDict[i] = Cave(i)
print(caveDict)
for i in input:
  if i[1] != "start":
    caveDict[i[0]].paths.append(caveDict[i[1]])
  if i[0] != "start":
    caveDict[i[1]].paths.append(caveDict[i[0]])

def numOfPaths(caveName = "start",passedThrough = []):
  this = caveDict[caveName]
  this.passes += 1
  if caveName == "end":
    
    print(passedThrough)
    return 1
  ans = 0
  nPassedThrough = []
  for i in passedThrough:
    nPassedThrough.append(i)
  nPassedThrough.append(caveName)
  for i in this.paths:
    if i.bigCave == False and i.passes < 3:
      ans += numOfPaths(i.name,nPassedThrough)
  this.passes -= 1
  return ans
print(caveDict["start"].paths)
print(numOfPaths())