# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

max = 2000000
new_max = (max - 2) // 2
marked = [False for x in range(new_max + 1)]
sieve = lambda x, y: x + y + 2 * x * y

for i in range(1, new_max):
       j = i
       while sieve(i, j) <= new_max:
           marked[sieve(i, j)] = True
           j += 1

acc = 0
for i, x in enumerate(marked):
    if i == 0:
        continue
    if i == 1:
        acc += 2
    if not x:
        acc += 2 * i + 1
print(acc)

