#Count digits in an integer

#Loop based(time complexity= O(Log10(n)))

def count(num):
    c=0
    while num>0:
        c+=1
        num = num//10
    print(c)
count(7569246820)

##LOG Approach.(time complexity= o(1) )

from math import *
def logcount(n):
    print(int(log10(n)+1))
logcount(789456123357159)
