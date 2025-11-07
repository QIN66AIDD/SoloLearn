# set a function as string
x = 'range(999)'
counter = 0

#print(eval(x))

# pass the string function into eval
for i in eval(x):
	x = 'range(1000)'
	counter += 1
print(counter)


'''output:

999
'''