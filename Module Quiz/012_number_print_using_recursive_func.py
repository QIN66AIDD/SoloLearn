# recursive function
def func(n):
	if n > 0:
		func(n - 1)
	print(n, end=' ')
	
# enter a number
x = int(input('Enter number : '))
func(x)


'''output:

Enter number : 10
0 1 2 3 4 5 6 7 8 9 10
'''