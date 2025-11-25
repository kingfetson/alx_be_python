class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print("\n--- Product Information ---")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: {self.total_value()}")
        print("---------------------------")


# Trigger user input (similar to Exercise 1)
name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

# Create Product object
product = Product(name, price, quantity)

# Display the product details
product.display_info()
