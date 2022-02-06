def fibonacci(n):
    if n == 1 or n == 0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for n in range(2000):
    print(fibonacci(n))