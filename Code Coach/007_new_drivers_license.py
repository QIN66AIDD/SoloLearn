'''
You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

Task:
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.
'''

name = input()
agent = int(input())
client = input().split()

client.append(name)
client.sort()

print(int(client.index(name)//agent)*20 + 20)