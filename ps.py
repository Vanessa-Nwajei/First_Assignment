def partial_sort(n,a,k):
    result = []
    if len(a) == n:
        while len(result)!=k:
            minimum = min(a)
            result.append(minimum)
            a.remove(minimum)
        return result

n = 10
a = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
k = 3

smallest_elements = partial_sort(n,a,k)
print(smallest_elements)