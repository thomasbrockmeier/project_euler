# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

i = 2
n = 600851475143 
while i < n:
    if not n % i:
        n, i = n // i, 2
    else:
        i += 1
print(n)

