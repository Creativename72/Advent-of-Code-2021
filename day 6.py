input = ""
with open('input.txt','r') as inp:
  for line in inp:
      input = line

input = input.split(",")
for i in range(len(input)):
  input[i] = int(input[i])
memoization = {}
def runDay(arr):
  for i in range(len(arr)):
    arr[i] -= 1
    if arr[i] == -1:
      arr[i] = 6
      arr.append(8)
  return arr
def runxdays(num,x):
  ogArr = num
  arr = [num]
  if num in memoization:
    return memoization[num]
  for i in range(x):
    arr = runDay(arr)
  memoization[num] = arr
  return arr
def runlenxdays(num,x):
  ogArr = num
  arr = [num]
  if num in memoization:
    return len(memoization[num])
  for i in range(x):
    arr = runDay(arr)
  memoization[num] = arr
  return len(arr)
x = 128
nInput = []
for j in input:
  nInput += runxdays(j,x)
input = nInput
ans = 0
for num in input:
  ans += runlenxdays(num,x)
print(ans)