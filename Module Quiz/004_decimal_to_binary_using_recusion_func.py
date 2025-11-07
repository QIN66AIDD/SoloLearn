def convert(num):
   if num == 0: return 0
   return (num % 2 + 10 * convert(num // 2)) 

num = int(input('Enter decimal number: '))
print('Decimal to binary:', convert(num))


'''output:

Enter decimal number: 8
Decimal to binary: 1000
'''