'''
input:
    blue
output:
    total of data = 118
    blue position = 1
    so, blue value of data = 43(11+36)
    percentage of value = 36%(43/118)*100
'''

data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]

color = input()
c = ['brown', 'blue', 'green', 'black']
total = 0
for x in data:
  total += sum(x)

for x in range(len(c)):
  if c[x]==color:
      result = int(((data[0][x]+data[1][x])/total)*100)
      print(result)