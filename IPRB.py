def mendel_first_law(k, m, n):

    # k : homozygous dominant
    # m : heterozygous 
    # n : homozygous recessive

    total_population = k + m + n

    #probability of selecting 2 recessive individuals
    probability_2_homozygous_recessive =(n / total_population) * ((n - 1) / (total_population - 1)) * 0
    #probability of selecting 2 dominant individuals
    probability_2_homozygous_dominant = (k / total_population) * ((k-1) / (total_population-1)) * 1
    #probability of selecting 2 heterozygous individuals
    probability_2_heterozygous = (m / total_population) * ((m-1) / (total_population-1)) * 0.75
    #probability of selecting a dominant and recessive individual
    probability_dominant_and_recessive = (k / total_population) * (n / (total_population-1)) * 1
    #probability of selecting a dominant and heterozygous individual
    probability_dominant_and_heterozygous = (k / total_population) * (m / (total_population-1)) * 1
    #probability of selecting a recessive and heterozygous individual
    probability_recessive_and_heterozygous = (m / total_population) * (n / (total_population-1)) * 0.5

    total = probability_2_heterozygous + probability_2_homozygous_dominant + probability_2_homozygous_recessive + probability_dominant_and_heterozygous + probability_dominant_and_recessive + probability_recessive_and_heterozygous
    return total

k = 2
m = 2
n = 2
print(f"{mendel_first_law(k,m,n)}")

# i couldn't get it :(