class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


# Example usage:
product1 = Product("Laptop", 750, 3)

print(f"Total value in stock: {product1.total_value()}")
