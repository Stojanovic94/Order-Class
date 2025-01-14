class Order:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        self.items = ['product1', 'product2', 'product3']  # Primer stavki

    def calculate_total(self):
        if not isinstance(self.price, (int, float)) or not isinstance(self.quantity, (int, float)):
            raise TypeError("Cena i količina moraju biti brojevi.")
        return self.price * self.quantity

    def get_items(self):
        return self.items  # Vraća listu proizvoda
