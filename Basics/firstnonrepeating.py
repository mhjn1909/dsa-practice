#Given a string, find the first character that appears only once.
s = "aabbcddee"
#Brute force
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count == 1:
        print("First non-repeating character:", s[i])
        break
#Optimal Approach
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for x in s:
    if freq[x] == 1:
        print("First non-repeating character:", x)
        break