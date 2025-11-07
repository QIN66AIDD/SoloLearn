'''
You have a bowl on your counter with an even number of pieces of fruit in it. Half of them are bananas, and the other half are apples. You need 3 apples to make a pie.

Task:
Your task is to evaluate the total number of pies that you can make with the apples that are in your bowl given to total amount of fruit in the bowl.
'''

fruit = int(input())

def apple(data):
    data = data//2
    return data
b = apple(fruit)
print (b // 3)