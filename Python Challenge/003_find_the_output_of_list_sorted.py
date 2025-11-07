# find the output of list sorted

my_list = ['car', 'plane', 'train', 'bike', 'rocket']
new_list = sorted(my_list, key=lambda x:x[-2])

print('Original list:', my_list)
print('New list:', new_list)


'''output:

Original list: ['car', 'plane', 'train', 'bike', 'rocket']
New list: ['car', 'rocket', 'train', 'bike', 'plane']
'''