#Amelia Chwee S10273205G
numbers = []
total = 0

while True:
    number = int(input("Please enter a number (0 to end): "))
    if number == 0:
        break
    else:
        numbers.append(number)
        total += number

odd = []
even = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

average = total / len(numbers)

print(f"Odd numbers: {odd}")
print(f"Even numbers: {even}")
print(f"Average = {average:.2f}")