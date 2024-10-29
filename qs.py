def quick_sort(n,arr):
    if len(arr) == n:
        arr.sort()
        return arr
    else:
        raise ValueError('Lenght of array either too long or too short') 
    
n = 7
a = [5, -2, 4, 7, 8, -10, 11]
result = quick_sort(n,a)
print(*result)