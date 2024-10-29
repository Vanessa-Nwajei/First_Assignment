def merge_two_sorted_arrays(n,A,m,B):
    C = []
    if len(A) == n and len(B) == m:
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1

        while i < len(A): # incase A has more elements than B, its appends the elemnts to C
            C.append(A[i])
            i += 1

        while j < len(B): # incase B has more elements than A, its appends the elemnts to C
             C.append(B[j])
             j += 1
        return C

n = 4
a = [2, 4, 10, 18]
m = 3
b = [-5, 11, 12]
merge = merge_two_sorted_arrays(n,a,m,b)
print(merge)