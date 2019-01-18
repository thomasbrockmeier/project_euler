# Lattice paths
# Problem 15 
# Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# 
# How many such routes are there through a 20×20 grid?

def fact(x):
    return x if x == 0 or x == 1 else x * fact(x-1)


def binomial(n, k): 
    return fact(n) // (fact(k) * fact(n - k)) 


n = k = 20
print(binomial(n + k, k))

