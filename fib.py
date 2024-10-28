def rabbits(n,k):
    #n : the number of months
    #k : the number of rabbits pairs
    if n <= 2:
        return 1
    else:
        return rabbits(n-1, k) + k * rabbits(n-2, k)
    

n = 36
k = 2
totalpairs= rabbits(n,k)
print(totalpairs)