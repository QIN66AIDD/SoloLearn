'''
You and three friends go to a baseball game and you offer to go to the concession stand for everyone. They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task:
Determine the total cost of ordering four items from the concession stand. If one of your friend's orders something that isn't on the menu, you will order a Coke for them instead.
'''

orders_list = list(x.strip() for x in input().split())
sum = 0.00

for x in orders_list:
    if x == 'Nachos' or x == 'Pizza':
        sum += 6
    elif x == 'Cheeseburger':
        sum += 10
    elif x == 'Water':
        sum += 4
    elif x == 'Coke':
        sum += 5
    else: sum += 5
    
print(sum + (sum*7)/100)