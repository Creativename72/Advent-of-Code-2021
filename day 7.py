import statistics
input = ""
with open('input.txt','r') as inp:
  for line in inp:
      input = line
input = input.split(",")
#print(input)
for i in range(len(input)):
  input[i] = int(input[i])
def fuelCost(x1,x2):
  d = abs(x2 - x1)
  return int((d) * (d+1)/2)

storageDict = {}
def totalFuelCost(alignment):
  if alignment in storageDict:
    return storageDict[alignment]
  tFuel = 0
  for i in input:
    tFuel += fuelCost(i,alignment)
  storageDict[alignment] = tFuel
  return tFuel

valueToCheck = statistics.median(input)
last = valueToCheck - 1
while True:
  if totalFuelCost(valueToCheck + 1) < totalFuelCost(valueToCheck):
    if valueToCheck + 1 == last:
      break;
    last = valueToCheck
    valueToCheck += 1
  else:
    if valueToCheck - 1 == last:
      break;
    last = valueToCheck
    valueToCheck -= 1
print(totalFuelCost(valueToCheck))