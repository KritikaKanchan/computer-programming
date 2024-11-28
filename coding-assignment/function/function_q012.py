#Write a function that returns the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
