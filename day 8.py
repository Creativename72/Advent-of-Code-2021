import itertools

#parses data
input = []
with open('input.txt','r') as inp:
  for line in inp:
      input.append(line)
for line in range(len(input)):
  input[line] = input[line].split(" | ")
for line in input:
  line[1] = line[1].split(" ")
'''   
 0000    
1    2
1    2 
 3333 
4    5 
4    5 
 6666
'''
#list of what is on in each number
dictionairy = {0:[0,1,2,4,5,6],1:[2,5],2:[0,2,3,4,6],3:[0,2,3,5,6],4:[1,2,3,5],5:[0,1,3,5,6],6:[0,1,3,4,5,6],7:[0,2,5],8:[0,1,2,3,4,5,6],9:[0,1,2,3,5,6]}

segmentList = ["a","b","c","d","e","f","g"]
permutations_object = itertools.permutations(segmentList)
segmentList = list(permutations_object)


#takes list of signals and determines a key for breaking the cipher
def breakCode(line):
  for i in segmentList:
    if codeWorksAllKeys(i,line):
      return i

#given a single key, checks if the signals make sense
def codeWorksAllKeys(key,line):
  for word in line.split(" "):
    if not codeWorksOneKey(key,word):
      return False
  return True

#given a single key, check if a single number makes sense
def codeWorksOneKey(key,word):
  checkerList = []
  for char in word:
    checkerList.append(key.index(char))
  checkerList.sort()
  return checkerList in dictionairy.values()

#given a key, returns what all the signlas mean
def decryptWords(key,line):
  nums = ""
  for word in line:
    nums += str(decryptWord(key,word))
  return int(nums)

#givena  key, returns what one word means
def decryptWord(key,word):
  checkerList = []
  for char in word.strip():
    checkerList.append(key.index(str(char)))
  checkerList.sort()
  return list(dictionairy.keys())[list(dictionairy.values()).index(checkerList)]

def main():
  finalAnswer = 0
  for line in input:
    key = breakCode(line[0])
    finalAnswer += decryptWords(key,line[1])
  print(finalAnswer)
main()