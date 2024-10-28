def rabbits(n,k):
    #n : the number of months
    #k : the number of the pairs of rabbits
    f1, f2 = 1, 1
    for i in range(2,n):
        current = f1 + k * f2
        f2 = f1
        f1 = current
    return current


n = 36
k = 2
totalpairs= rabbits(n,k)
print(totalpairs)