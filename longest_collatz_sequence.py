# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(n): 
    def _collatz(i): 
        x = solutions.get(i)
        if not x:
            if not i % 2:
                x = 1 + _collatz(i // 2) 
            else:
                x = 2 + _collatz((3 * i + 1) // 2)
            solutions[i] = x
        return x

    longest_chain = 0 
    solutions = {1: 1} 
    for x in range(n // 2, n): 
        new_chain = _collatz(x) 
        if new_chain > longest_chain: 
            longest_chain = new_chain 

    for k, v in solutions.items(): 
        if v == longest_chain: 
            return k

target = 1000000
print(collatz(target))

