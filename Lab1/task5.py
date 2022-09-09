def PrintMenu():
    menu = ['1 - View discription', '2 - View Price', '3 - View Amount', '4 - View all Inforamtion', '5 - Shop', 'else - exit']    
    for i in range(len(menu)):
        print("#%d %s" % (i + 1, menu[i]))
    choice = int(input("\nInput your choice: "))
    return choice

wheel = [['железо', 'резина'], 123, 10]
fara = [['стекло', 'светодиоды'], 89, 8]
shop = {'колесо' : wheel, 'фары' : fara}

while (True):
    choice = PrintMenu()
    if choice == 1:
        for key_name, value in shop.items():
            print(key_name, "->", value[0])
    elif choice == 2:
        for key_name, value in shop.items():
            print(key_name, "->", value[1])
    elif choice == 3:
        for key_name, value in shop.items():
            print(key_name, "->", value[2])
    elif choice == 4:
        for key_name, value in shop.items():
            print(key_name, "->", value)
    elif choice == 5:
        input_name = input("Input name of item: ")
        value = shop.get(input_name)
        if value is None:
            print("there is no such product in the store!")
        else:
            amount = int(input("Input amount:"))
            if amount > value[2]:
                print("There is store out of stock, you will buy all available items!")
            final_price = min(amount, value[2]) * value[1]
            value[2] = max(value[2] - amount, 0)
            print("Final price:", final_price)
    else:
        print("Do svidaniya")
        break;
