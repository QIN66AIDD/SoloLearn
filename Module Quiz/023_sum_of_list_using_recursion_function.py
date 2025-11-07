def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0]**2 + calc(list[1:])

list = [1, 3, 4, 2, 5] # 1**2=1, 3**2=9, 4**2=16, 2**2=4, 5**2=25
x = calc(list)        
print(x)


'''output:

55
'''