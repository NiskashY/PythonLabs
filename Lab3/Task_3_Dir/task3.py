database_filename = "database.txt"


dict_disciplines = {}
with open(database_filename, "r") as data:
    for discipline in data:
        discipline_list = list(discipline.split())
        list_len = len(discipline_list)
        dict_disciplines[discipline_list[0]] = discipline_list[1:list_len]

for key, value in dict_disciplines.items():
    print(f"{key} : {value}")
