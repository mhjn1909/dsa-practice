#Check for palindrome(same left to right and right to left. ex- nitin=nitin)
#(Time complexity= O(log10(n)))
def palindrome(num):
    original = num
    rev=0
    last=0
    while(num>0):
        last=num%10
        rev=(rev*10)+last
        num=num//10
    print(rev)
    if original == rev:
        print('Palindrome')
    else:
        print("Not")
palindrome(4224)