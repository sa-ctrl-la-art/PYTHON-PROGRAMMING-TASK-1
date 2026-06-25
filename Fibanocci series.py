print("Fibanocci Series")
def fibonacci_loop(n):
    sequence =[]
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
num = int(input("Enter how many Fibonacci numbers to generate: "))
print(f"First {num} Fibonacci numbers: {fibonacci_loop(num)}")
