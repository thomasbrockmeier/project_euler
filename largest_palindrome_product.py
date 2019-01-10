# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
n = 999 ** 2 + 1

while n:
    n -= 1
    s = str(n)
    if s == s[::-1]:
        for x in range(100, 1000):
            if not n % x and 100 <= (n / x) < 1000:
                print(n)
                n = 0
                break

