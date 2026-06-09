#Given an integer array arr and an integer target, count the number of pairs whose sum is equal to target.
arr = [1,5,7,-1,5]
target = 6
#Brute Force (O(n**2))
count=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==target):
            count+=1
print(count)

#Optimal Approach (O(n))
hash_map={}
count=0
for x in arr:
    need=target-x
    if need in hash_map:
        count += hash_map[need]
    if x in hash_map:
        hash_map[x] += 1
    else:
        hash_map[x] = 1
print(count)

