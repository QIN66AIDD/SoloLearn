# letter frequency, how many letter store in text

txt = input()
ch  = input()

counter = 0
for x in txt:
    if x == ch:
        counter += 1
print(int((counter/len(txt)*100)))