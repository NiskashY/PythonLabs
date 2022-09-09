input_count = int(input("Input total number of elements: "))
given_list = []
#given_list = [1.34, '1qwerty', 12, 13, 16, 'Love', 'Python']

for i in range(input_count):
    input_value = input("Enter value: ")
    if input_value.isdecimal():
        input_value = int(input_value)
    given_list.append(input_value)
    

numbers = []
words = []
final_sum = 0
final_mulitply = 1

for i in given_list:
    if type(i) == float:
        numbers.append(i)
        final_sum += i
        final_mulitply *= i
    elif type(i) == str:
        words.append(i)

print("Sum =", final_sum)
print("Multiply =", final_mulitply)
numbers.sort()

for i in range(len(numbers) - 1, max(len(numbers) - 4, -1), -1):
    print(numbers[i], end = ' ')
print()
