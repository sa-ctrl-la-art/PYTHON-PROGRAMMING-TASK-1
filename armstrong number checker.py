print("armstrong number checker")
num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)
if num == total:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
