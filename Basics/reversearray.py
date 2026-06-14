#Reverse an array using recursion b/w given indices (left,right)
def func(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    return func(arr,left+1,right-1)
arr = [5,7,3,2,6,1,5,9]
func(arr,2,5)
print(arr)