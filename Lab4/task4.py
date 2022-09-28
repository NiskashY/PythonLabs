class database:
    __count = 0
    __memory = []

    def __init__(self, memory):
        self.__memory.append(memory)
        self.__count += 1

    def _getMemoryList(self):
        return self.__memory


class SQL:
    
    def __init__(self, tables, fields):
        tmp = tables * fields
        super().__init__(tmp)
        self.__tables = tables
        self.__fields = fields

    def getTotalMemory(self):
        return sum(super()._getMemoryList())
    

def main():
    sql = SQL(10, 29)
    print(sql.getTotalMemory())

if __name__:
    main()
