# LD 1st Code Notes on Recursion

# Understanging loops
for num in range(1,11):
    if num % 2 == 0:
        print(num)

even = []

num = 20
sum = 1
for x in range(1,num+1):
    sum *= x
print(f"Loop: {sum}")

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(f"Recursion: {factorial(num)}")

# Fibonacci  Sequence
fib = [1,1]

for i in range(1,11):
    fib.append(fib[i-1] + fib[i])

print("Fibonacci Sequence LOOP:")
print(fib)
def fibonacci(n):
    if n == 2: 
        return 1
    elif n == 1:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci Sequence RECURSION:")
print(fibonacci(11)) # Going to 10th digit in sequence