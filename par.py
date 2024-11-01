def two_way_partition(n, A_arr):
    B_arr = []
    first_element = A_arr[0]
    
    smaller_than_first_element = []
    larger_than_first_element = []

    if n == len(A_arr):
        for i in A_arr:
            if i < first_element:
                smaller_than_first_element.append(i)
            else:
                larger_than_first_element.append(i)

        B_arr = smaller_than_first_element + larger_than_first_element
        return B_arr

n = 9
m = [7,2,5,6,1,3,9,4,8]
partition = two_way_partition(n,m)

print(partition)