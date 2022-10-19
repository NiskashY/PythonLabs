class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def _getIncomeWithBonus(self):
        total_income = 0
        for characteristic, value in self.__income.items():
            total_income += value
        return total_income

    def _getFullName(self):
        return self.name + " " + self.surname


class Position(Worker):
    
    def __init__(self, name_, surname_, position_, income_):
        super().__init__(name_, surname_, position_, income_)

    def GetFullName(self):
        return super()._getFullName()

    def GetTotalIncome(self):
        return super()._getIncomeWithBonus()


def main():
    name = input("Input name: ")
    surname = input("Input surname: ")
    position = input("Input worker position: ")
    income = {"wage": 0, "bonus": 0}

    for characteristic, value in income.items():
        income[characteristic] = int(input(f"Input {characteristic}: "))

    pos = Position(name, surname, position, income)

    print(f"Worker Full Name: {pos.GetFullName()}")
    print(f"total worker income = {pos.GetTotalIncome()}")


if __name__:
    main()
