import json


def ParseInts(values):
    for i in range(2, len(values_list)):
        values_list[i] = int(values_list[i])
    return values


file_name = "database.txt"

companies = {}
average_profit = 0

with open(file_name, "r") as data:
    for company in data:
        values_list = list(company.split())
        values_list = ParseInts(values_list)
        companies[values_list[0]] = values_list[2] - values_list[3]
        if companies[values_list[0]] > 0:
            average_profit += companies[values_list[0]]

companies["average"] = average_profit / len(companies)

file_name_output = "ouput_data.json"

with open(file_name_output, "w") as out_file:
    json.dump(companies, out_file)
    json_str = json.dumps(companies)

print(f"Done!\nCheck file {file_name_output}\nParsed str:\n {json_str}")
