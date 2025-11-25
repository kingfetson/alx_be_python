class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: {self.total_value()}")
        print("-" * 30)

# Trigger user input
products = []

print("Enter product details (type 'stop' to finish):")
while True:
    name = input("Product Name: ")
    if name.lower() == "stop":
        break
    
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = Product(name, price, quantity)
    products.append(product)
    print("Product added!\n")

# Print all products
print("\n=== PRODUCT LIST ===")
for prod in products:
    prod.display_info()
