def three_way_partition(n, A_arr):
    B_arr = []
    first_element = A_arr[0]

    smaller_than_first_element = []
    larger_than_first_element = []
    equal_to_first_element = []

    if len(A_arr) == n:
        for i in A_arr:
            if i < first_element:
                smaller_than_first_element.append(i)

            elif i == first_element:
                equal_to_first_element.append(i)

            else:
                larger_than_first_element.append(i)

        B_arr = smaller_than_first_element + equal_to_first_element +  larger_than_first_element
        return B_arr
    
    else:
        return None

n = 9
m = [4,5,6,4,1,2,5,7,4]
partition = three_way_partition(n,m)

print(partition)