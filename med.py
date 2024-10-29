def median(n = int,arr = list,k = int):
    if len(arr) == n and k <= n:
        arr.sort()
        return arr[k-1]
    
n = 11
arr = [2,36,5,21,8,13,11,20,5,4,1]
k = 8
med = median(n,arr,k)
print(med)