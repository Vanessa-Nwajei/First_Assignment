def insertion_sort(n, arr):
    swap = 0
    for i in range(1, n):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
            swap += 1
        arr[j + 1] = k
    return swap
n = 6
arr = [6, 10, 4, 5, 1, 2]
swap_count = insertion_sort(n, arr)
print(swap_count)