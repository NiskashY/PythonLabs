class LowerThanZero(Exception):
    def __init__(self, message):
        super().__init__(message)


def InputMatrix(rows, columns):
    matrix = []
    print("Input matrix:")

    isNeedToExitInput = False
    while not isNeedToExitInput:
        try:
            for i in range(rows):
                row_list = list(input().split())
                if len(row_list) > columns:
                    raise ValueError
                matrix.append(row_list)
            isNeedToExitInput = True
        except ValueError:
            print("ReEnter:")

    return matrix


def FindFirstRow(matrix):
    for i in matrix:
        final_sum = 0
        cnt = 0
        for j in i:
            if j.isdigit() and int(j) > 0:
                cnt += 1
                final_sum += int(j)
        if cnt == len(i):
            return final_sum
    return None


isNeedToExit = False
rows_number = columns_number = 0
while not isNeedToExit:
    try:
        rows_number = int(input("Enter rows_number:"))
        columns_number = int(input("Enter columns_number:"))
        if rows_number <= 0 or columns_number <= 0:
            raise LowerThanZero("rows && columns must be greater than 0")
        isNeedToExit = True
    except LowerThanZero as e:
        print(e, end="\n\n")

matrix = InputMatrix(rows_number, columns_number)
value = FindFirstRow(matrix)
if value is None:
    print("No positiv row in matrix!")
else:
    print("Sum of first positive row =", value)
