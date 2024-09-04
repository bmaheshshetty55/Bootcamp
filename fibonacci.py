def fibonacci(n):
    # Create an array to store Fibonacci numbers
    fib = [0] * (n + 1)

    # Initial values
    fib[0] = 0
    fib[1] = 1

    # Build the Fibonacci series up to the nth number
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Input: the position in the Fibonacci series
n = int(input("Enter the position (n): "))

# Output: the nth Fibonacci number
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")