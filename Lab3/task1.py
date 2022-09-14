file_name = "data_1_task.txt"
with open(file_name, "w") as f_obj:
    input_message = "Enter string: "
    value = input(input_message)
    while len(value) != 0:
        f_obj.write(value + "\n")
        value = input(input_message)

with open(file_name, "r") as f_obj:
    file_name_dest = "data_1_task_dest.txt"
    max_length_word = ""
    with open(file_name_dest, "w") as dest_obj:
        for line in f_obj:
            value = list(line.split())
            if len(value) == 1:
                dest_obj.write(value[0] + "\n")
                if len(value[0]) > len(max_length_word):
                    max_length_word = value[0]
        dest_obj.write(f"\nmax_length_word = {max_length_word}")

print("\nDone!\nCheck file 'data_1_task_dest.txt' ")