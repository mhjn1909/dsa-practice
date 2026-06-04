#Check if number is armstrong no or not.
#Armstrong no- 153: 1 cube+5 cube+3 cube=153 (time complexity=log10(n))
def armstrong(num):
    n = num
    count=0
    total=0
    #Count Digits
    while (num>0):
        digit=num%10
        count+=1
        num=num//10
    num=n #resetting 
    #Armstrong
    while num > 0:
        digit = num % 10
        total = total + (digit ** count)
        num = num // 10
    if(n==total):
        print("Armstrong no.")
    else:
        print("not")
armstrong(153)    
