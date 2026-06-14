#Check if string is a palindrome by both loop and recursive approach
#1) Loop (TC=o(N))
s="NITIN"
n=len(s)
left=0
right=n-1
while left<right:
    if s[left] != s[right]:
        print(False)
        break
    left+=1
    right-=1
else:(print(True))

#2)Recursive (TC=0(N))
def func(x,l,r):
    if l>=r:
        return True
    if x[l] != x[r]:
        return False
    return func(x,l+1,r-1)
x='MOM'
print(func(x,0,2))