#code shortened as a challenge to do day in least lines of code
input,depth,horizontal,aim,d2,d1,inp = [],0,0,0,{"f":0,"d":1,"u":-1},{"f":1,"d":0,"u":0},open('input.txt')
for i in inp.read().split("\n"):
  horizontal,depth,aim := int(i[-1]) * d1[i[0]] + horizontal, int(i[-1]) * aim * d1[i[0]] + depth, int(i[-1]) * d2[i[0]] + aim
print(depth * horizontal)
