# A simple script
name = "World"
print(f"Hello, {name}!")

# List comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)  # Output: [1, 4, 9, 16]

def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n-1)

print(factorial(5)) # Output: 120
