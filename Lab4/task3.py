import abc


def getCoef(classType):
    if type(classType) == Airplane:
        return 0.1
    elif type(classType) == Train:
        return 0.5
    elif type(classType) == Car:
        return 0.7
    else:
        return 1


class Transport:
    def __init__(self, cost, distance, coef):
        self.__cost = cost
        self.__travel_distance = distance
        self.__k = coef

    @abc.abstractmethod
    def _getTime(self):
        return self.__travel_distance

    @abc.abstractmethod
    def getTravelCost(self):
        return self.__cost * (1 / self.__k) + self.__travel_distance * self.__k


class Airplane(Transport):
    def __init__(self, cost, dist):
        super().__init__(cost, dist, getCoef(self))


class Train(Transport):
    def __init__(self, cost, dist):
        super().__init__(cost, dist, getCoef(self))


class Car(Transport):
    def __init__(self, cost, dist):
        super().__init__(cost, dist, getCoef(self))


def main():
    dist = int(input("Enter distance: "))
    cost = int(input("Enter cost: "))

    train = Train(cost, dist)
    car = Car(cost, dist)
    airplane = Airplane(cost, dist)

    print(f"Train total_cost = {train.getTravelCost()}")
    print(f"Car total_cost = {car.getTravelCost()}")
    print(f"Airplane total_cost = {airplane.getTravelCost()}")


if __name__:
    main()
