#stock.py

class Stock:
    __slots__ = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
