class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f'{self.title} — {self.price} сом (остаток: {self.quantity})'

    def __repr__(self):
        return f'Product(title={self.title}, price={self.price}, quantity={self.quantity})'
    def __eq__(self, other):
        if self.title == other.title:
            return True
        return False
    def __lt__(self, other):
        if self.price < other.price:
            return True
        return False
    def __add__(self, other):
        return Product('Combo', self.price + other.price, 1)

p1 = Product("Клавиатура", 1500, 10)
p2 = Product("Клавиатура", 1800, 5)
p3 = Product("Мышка", 700, 20)

print(p1 == p2)      # True (название одинаковое)
print(p3 < p1)       # True (700 < 1500)
combo = p1 + p3
print(combo)