def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Факторіал 5:", factorial(7))
