#Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
nums = [2,17,7,11,15]
target = 9

#Brute Force(O(n**2))
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if((nums[i]+nums[j])==target):
           print([i,j])
           
#Optimal Approach(O(n))
hash_map={}
for x in range(len(nums)):
     complement = target - nums[x]
     if complement in hash_map:
        print([hash_map[complement], x])
        break
     hash_map[nums[x]] = x