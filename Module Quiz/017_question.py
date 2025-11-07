class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def next(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end': break
    c.add(n)

time = 0
while True:
  if c.is_empty(): break
  item = c.next()
  time +=5 if item=='general' else 10

print(time)


'''output:

1
1
2
5
end
50
'''