class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            values = line.split()
            self.lst_data.append(dict(zip(self.FIELDS, values)))

    def select(self, a, b):
        return self.lst_data[a:b + 1]