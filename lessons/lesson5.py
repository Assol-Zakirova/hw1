class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    @classmethod
    def from_string(cls, data):
        title, price = data.split(",")
        return cls(title, int(price))
    def __str__(self):
        return f'{self.title}, {self.price}'
p = Product.from_string("Клавиатура,1500")
print(p)