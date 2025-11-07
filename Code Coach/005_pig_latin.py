'''
You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in the same order except that you take the first letter of each word and put it on the end, then you add 'ay' to the end of that. ("road" = "oadray") 

Task:
Your task is to take a sentence in English and turn it into the same sentence in Pig Latin!
'''

words = list(x.strip() for x in input().split())

for x in range(len(words)):
    words[x] = words[x][1:]+words[x][0]+'ay'
    
print(' '.join(words))