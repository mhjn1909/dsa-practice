#Problem Statement: a string n and list m are given given. find how many time the elements of m are present in n. 
#Constraints: 'a'<=n[i]<= 'z'
n='azywqxyzbhjiplkabc'
m=['a','z','b','k']
val=[]
#Brute Force
for i in range(0,len(m)):
    count=0
    for j in range(0,len(n)):
        if m[i]==n[j]:
            count+=1
    val.append(count)
print(val)

#optimal
hash_list=[0]*26
for ch in n:
    ascii_val=ord(ch)
    index= ascii_val- 97
    hash_list[index]+=1
for char in m:
    asci= ord(char)
    ind= asci-97
    print(hash_list[ind])