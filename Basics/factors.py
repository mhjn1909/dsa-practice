#Print all factors of given no. 
#Brute force (time complexity=O(n))
def factor(num):
    digits=[]
    for i in range(1,num+1):
        if(num%i==0):
            digits.append(i)
        else:
            continue
    print("factors are:",digits)
factor(10)

#Better solution(Time complexity=O(n/2))
def factors(n):
    d=[]
    for j in range(1,(n//2)+1):
        if(n%j==0):
            d.append(j)
        else:
            continue
    d.append(n)
    print("factors are:",d)
factors(10)

#Optimal Solution(Time Complexity= O(sqrt(x)))
from math import sqrt
def fact(x):
    result=[]
    for i in range(1,int(sqrt(x)+1)):
        if x%i==0:
            result.append(i)
            if x//i != i:
                result.append(x//i)
    result.sort()
    print(result)
fact(100)