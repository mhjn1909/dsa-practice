#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
nums = [100,4,200,1,3,2]
#Brute Force(O(n**2))
longest = 0
for num in nums:
    current = num
    count = 1
    while current + 1 in nums:
        current += 1
        count += 1
    longest = max(longest, count)
print(longest)

#Optimal Approach (O(n))
num_set = set(nums)
long = 0
for i in num_set:
    if i- 1 not in num_set:
        current = i
        count = 1
        while current + 1 in num_set:
            current += 1
            count += 1
        long = max(long, count)
print(long)

