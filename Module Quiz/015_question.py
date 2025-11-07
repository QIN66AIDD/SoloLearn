'''
input:
    python

output:
    p
    yy
    ttt
    hhhh
    ooooo
    nnnnnn
'''

txt = input()

i=0

while i<len(txt):
    print(txt[i]*(i+1))
    i += 1