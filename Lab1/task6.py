from cmath import inf

input_values = input("Enter some values: ")
input_tuple = tuple(input_values.split())

max_element = inf
for i in range(len(input_tuple)):
    if i % 2 and input_tuple[i].isdigit():
        value = int(input_tuple[i])
        max_element = min(max_element, value)

if max_element is inf:
    print(input_tuple[0])
else:
    print(max_element)

    
