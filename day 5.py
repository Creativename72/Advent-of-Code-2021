input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line)
map = []
dimensions = 2000
for i in range(dimensions):
  map.append([])
  for j in range(dimensions):
    map[i].append(0)

class line:
  def __init__(self,str):
    split1 = str.split(" -> ")
    coords1 = split1[0].split(",")
    coords2 = split1[1].split(",")
    self.x1 = int(coords1[0])
    self.y1 = int(coords1[1])
    self.x2 = int(coords2[0])
    self.y2 = int(coords2[1])
  def draw(self):
    xstep = 1
    ystep = 1
    if self.x1 > self.x2:
      xstep = -1
    if self.y1 > self.y2:
      ystep = -1
    
    if self.x1 == self.x2:
      for i in range(self.y1,self.y2 + ystep, ystep):
        map[self.x1][i] += 1
    elif self.y1 == self.y2:
      for i in range(self.x1,self.x2 + xstep, xstep):
        map[i][self.y1] += 1
    elif abs(self.x1 - self.x2) == abs(self.y1-self.y2):
      x = self.x1
      y = self.y1
      for i in range(abs(self.x2-self.x1) + 1):
        map[x][y] += 1
        x += xstep
        y += ystep
        
def scoreDiagram():
  ans = 0
  for i in map:
    for j in i:
      if j >= 2:
        ans += 1
  return ans

def main():
  for i in input:
    ln = line(i)
    ln.draw()
  print("answer is equal to:", scoreDiagram())
main()