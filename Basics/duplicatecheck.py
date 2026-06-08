#Given an array, return True if any element appears more than once, otherwise False.
arr=[1,5,9,7,8,6,5,1,3]
#Brute Force
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(True)
        
#Optimal approach
arr = [1,2,3,4,2]
seen = set()
duplicate = False
for num in arr:
    if num in seen:
        duplicate = True
        break
    seen.add(num)
print(duplicate)
    




        