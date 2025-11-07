file = open('file_name.txt', 'r')


results = file.readlines()
for x in results:
    print(x[0]+str(len(x.rstrip())))

file.close()