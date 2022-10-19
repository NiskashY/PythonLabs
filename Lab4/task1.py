class String:
    __string_count = 0

    def __init__(self):
        self.__string_count += 1
        self.__storage = "Hello, my dear friend"
        print(f"{self.__storage}, now you have {self.__string_count} strings")

    def __del__(self):
        self.__string_count -= 1

    def getString(self):
        return self.__storage

    def setString(self, new_string):
        self.__storage = new_string

    def Concatenate(self, value):
        self.__storage += str(value)
    
    def CalculateSymbols(self):
        symbols_count = 0
        for item in self.__storage:
            if item != ' ':
                symbols_count += 1
        return symbols_count

    def Clear(self):
        self.__storage = ""

    def Multiply(self, times): # return __storage + __storage + ... + __storage
        new_string = ""
        for i in range(times):
            new_string += self.__storage
        return new_string

    def Divide(self, value):
        # return list (with size of (length(storage) // value)
        # of new strings with length exactly value
        # if (length < value) : return copy of string
        new_strings_number = len(self.__storage) // value
        list_of_new_string = []
        prev_index = 0
        for i in range(new_strings_number):
            list_of_new_string.append(self.__storage[prev_index:prev_index + value])
            prev_index += value

        return list_of_new_string


some_str = String()
some_str.Clear()
some_str.Concatenate("aaaa")
some_str.Concatenate("bbbb")
print(some_str.Divide(3))
