'''
You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

Task:
Evaluate the area of two different balconies and determine which one is bigger.
'''

a = input().split(',')
b = input().split(',')

x = int(a[0]) * int(a[1])
y = int(b[0]) * int(b[1])

if x > y: print('Apartment A')
else: print('Apartment B')