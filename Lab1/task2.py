text = input("Input text: ")

vowels = "aeiouy"
vowels_numbers = connsonant_numbers = 0
vowels_list = []
for i in text:
    if i in vowels:
        vowels_numbers += 1
        vowels_list.append(i)
    elif i.isalpha() and i != ' ':
        connsonant_numbers += 1

print(vowels_numbers, connsonant_numbers)
if vowels_numbers == connsonant_numbers:
    for i in vowels_list:
        print(i, end=' ')
print()

