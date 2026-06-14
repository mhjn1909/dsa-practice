#print integer x, n times using recursion
def print_num(x,n):
    if n==0:
        return
    print(x)
    print_num(x,n-1)
print_num(1,5)


# Print numbers from 1 to x using recursion
def num(i, x):
    if i > x:
        return
    print(i)
    num(i + 1, x)
num(1, 5)