# default sentence
x ='this is test'

# use built-in function
print(x.title())

# use custom
print(' '.join([i[0].upper()+i[1:] for i in x.split()]))


'''output:

This Is Test
This Is Test
'''