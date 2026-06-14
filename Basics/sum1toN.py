#Print sum of of 1 to N integers using functional recursion
def func(n):
    if n==1:
        return 1
    return n+func(n-1)
print(func(10))