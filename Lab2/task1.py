def IsPrime(number):
    for i in range(2, number):
        if i * i > number:
            break

        if number % i == 0:
            return False
    return True


isNeedToExit = False
while isNeedToExit is False:
    try:
        input_value = int(input("Input number: "))
        isNeedToExit = True
    except ValueError:
        print("Input integer number! ReEnter:", end=' ')
    else:
        print("Is prime?", IsPrime(input_value), end=' ')
    finally:
        print("\n")
    
