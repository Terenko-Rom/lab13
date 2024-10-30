class Sweet:
    def __init__(self, name, price, producer):
        self.name = name
        self.price = price
        self.producer = producer
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def set_producer(self, producer):
        self.producer = producer
    def display(self):
        print(f"Назва: {self.name}, Ціна: {self.price}, Виробник: {self.producer}")
    def get_price(self):
        return self.price
sweet_list = [
    Sweet("Шоколад", 50, "Рошен"),
    Sweet("Цукерки", 30, "Київ"),
    Sweet("Печиво", 20, "Світоч")
]
for sweet in sweet_list:
    sweet.display()