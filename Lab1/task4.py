input_string = input("Input string: ")

dictionary = {}
for item in input_string:
    some_value = dictionary.get(item)
    if some_value is None:
        some_value = 0
    dictionary[item] = some_value + 1

for i in dictionary:
    print("'%c' = %d" % (i, dictionary[i]))

