print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Initialize the first two Fibonacci numbers
a, b = 1, 2
total = 0

# Print the first Fibonacci number
print(a, end=" ")

# Generate Fibonacci numbers less than 4,000,000
while a <= 4000000:
    if a % 2 == 0:  # Check if the number is even
        total += a
    print(a, end=" ")  # Print the Fibonacci number
    a, b = b, a + b  # Update to the next Fibonacci numbers

# Print the sum of even Fibonacci numbers
print("\nSum of even numbers in Fibonacci series:", total)
