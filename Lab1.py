number = int(input("Input intger number: "))

for i in range(1, number):
    if i * i > number:
        break

    if number % i == 0:
        print(i, end = " ")
        number //= i

if number > 1:
    print(number, end = " ")

print()
