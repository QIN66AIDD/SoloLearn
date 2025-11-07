'''
You are getting ready to paint a piece of art. The canvas and brushes that you want to use will cost 40.00. Each color of paint that you buy is an additional 5.00. Determine how much money you will need based on the number of colors that you want to buy if tax at this store is 10%.

Task:
Given the total number of colors of paint that you need, calculate and output the total cost of your project rounded up to the nearest whole number.
'''

import math

cost = 40.00
xbuy = 5.00

x = int(input())

total = cost + (xbuy * x)
tax   = (total * 10) / 100
print(math.ceil(total + tax))