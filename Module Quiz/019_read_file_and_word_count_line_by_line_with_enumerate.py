
with open("file_name.txt") as f:
   l = f.readlines()

for line, txt in enumerate(l, start=1): # start counting 1
   print('Line {}: {} words'.format(line, len(txt.split())))
f.close()