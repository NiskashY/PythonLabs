amount_of_members = 500

right_part_number_pi = 0 
numerator = denominator = 1
for i in range(amount_of_members):
    if i % 2:
        right_part_number_pi -= numerator / denominator
    else:
        right_part_number_pi += numerator / denominator

    denominator += 2

print(right_part_number_pi * 4)
