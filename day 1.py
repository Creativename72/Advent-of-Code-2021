input = []
with open('input.txt','r') as inp:
  for line in inp:
    print(line)
    print(line.index("@"))
    input.append(line[line.index("@") + 1:-1])
grid = []
for i in range(1000):
  grid.append([])
  for j in range(1000):
    grid[i].append(0)
