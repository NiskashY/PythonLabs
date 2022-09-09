def CheckForType(value):
    if type(value) == list:
        final_sum = 0
        for i in value:
            if i.isdigit():
                final_sum += int(i)
        print("Sum of list =", final_sum)
    elif type(value) == dict:
        values_list = list(value.values())
        values_list.sort()
        size = len(values_list)
        print("MAx elements:", end=' ')
        for i in range(size - 1, max(size - 4, -1), -1):
            print(values_list[i], end=' ')
        print()
    elif type(value) == int:
        value_digit_sum = 0
        while value:
            value_digit_sum += value % 10
            value //= 10
        print("SUm of digits:", value_digit_sum)
    elif type(value) == str:
        words_list = list(value.split())
        print(len(words_list))
    else:
        print("Ogog Kakoi-to tip")


input_value = input("Enter value: ")
try:
    input_value = int(input_value)
except ValueError:
    try:
        result = dict((a.strip(), int(b.strip()))
                      for a, b in (element.split('-')
                                   for element in input_value.split(', ')))

        input_value = result
    except ValueError:
        try:
            input_value = list(input_value.split())
        except ValueError:
            input_value = str(input_value)
finally:
    CheckForType(input_value)
