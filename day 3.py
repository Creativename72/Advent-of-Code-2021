
input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line.strip())
print(input)
commonArray = []
for i in range(len(input[0])):
  commonArray.append(0)

for line in input:

  for char in range(len(line)):
    if line[char] == "1":
      commonArray[char] += 1
    else:
      commonArray[char] -= 1

for i in range(len(commonArray)):
  if commonArray[i] > 0:
    commonArray[i] = "1"
  else:
    commonArray[i] = "0"

ans = ""
antians = ""
invDict = {"0":"1","1":"0"}
for i in commonArray:
  ans += i
for i in commonArray:
  antians += invDict[i]

def oxygenGeneratorRating(input, digit):
  if len(input) == 1:
    return input[0]
  ones = []
  zeroes = []
  for i in input:
    bit = i[digit]
    if bit == "1":
      ones.append(i)
    else:
      zeroes.append(i)
  if len(zeroes) > len(ones):
    return oxygenGeneratorRating(zeroes, digit + 1)
  else:
    return oxygenGeneratorRating(ones, digit + 1)
def carbonGeneratorRating(input, digit):
  if len(input) == 1:
    return input[0]
  ones = []
  zeroes = []
  for i in input:
    bit = i[digit]
    if bit == "1":
      ones.append(i)
    else:
      zeroes.append(i)
  if len(zeroes) > len(ones):
    return carbonGeneratorRating(ones, digit + 1)
  else:
    return carbonGeneratorRating(zeroes, digit + 1)

print(int(carbonGeneratorRating(input,0),2) * int(oxygenGeneratorRating(input,0),2))