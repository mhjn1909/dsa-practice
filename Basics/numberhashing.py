#Problem Statement: two lists n,m are given. find how many time the elements of m are present in n. 
#Constraints: 1<=n[i]<= 10, m and n can have 10**8 elements.
#Brute Force
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
val =[]
#Brute Approach
for i in range (0,len(m)):
    count=0
    for j in range (0,len(n)):
        if (m[i]==n[j]):
            count+=1
    val.append(count)
print(val)

#Optimal approach
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for x in m:
    if x<0 or x>10:
        print(0)
    else:
        print(hash_list[x])

#Using Dictionary
freq={}
ans=[]
for y in range(0,len(n)):
    if n[y] in freq:
         freq[n[y]]+=1
    else:
        freq[n[y]]=1
for w in range (0,len(m)):
    if m[w] in freq:
         ans.append(freq[m[w]])
    else:
        ans.append(0)
print(ans)