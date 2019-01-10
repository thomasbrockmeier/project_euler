# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if not n % 2 or not n % 3:
        return False
    i = 5
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


c = i = 0

while c < 10001:
    i += 1
    if is_prime(i):
        c += 1
print(i)

