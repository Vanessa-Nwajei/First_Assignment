def hamming_distance(t,s):
    #check that the lengths of the two strings are equal or else raise value error
    if len(t) != len(s):
        raise ValueError('Strings must have equal lenght')
    
    distance = 0
    for i in range(len(s)):
        if t[i] != s[i]:
            distance += 1
    return distance

s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
distance = hamming_distance(s,t)
print(distance)