class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        result = []

        for gd in self.goods:
            result.append(f"{gd.name}: {gd.price}")

        return result

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

tv1 = TV("Samsung", 50000)
tv2 = TV("LG", 45000)

table = Table("Стол", 10000)

notebook1 = Notebook("ASUS", 60000)
notebook2 = Notebook("Lenovo", 55000)

cup = Cup("Кружка", 500)

cart = Cart()

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(notebook1)
cart.add(notebook2)
cart.add(cup)

print(cart.get_list())