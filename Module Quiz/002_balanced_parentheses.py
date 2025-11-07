def balanced(expression):
    count = 0
    for ch in expression:
        if ch == '(':
            count += 1
        elif ch == ')':
            if count == 0:
                return False
            count -= 1
    return count == 0
    

x = '(x+y)*(x-z)-9'
print(balanced(x))


'''output:

True
'''