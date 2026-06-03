#Extract digits from a number
def extract_digits(num):
    digits=[]
    while num>0:
        digit=num%10
        digits.append(digit)
        num=num//10
    print("Digits extracted:", digits)
extract_digits(58761)