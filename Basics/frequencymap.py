#Store frequency of each digit of num array in dictionary
num=[123,4,5,9,8,7,6,1,2,3,7,5,6,2,5,4,789]
freq_map={}
for i in range(0,len(num)):
    if num[i] in freq_map:
         freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1
print(freq_map)