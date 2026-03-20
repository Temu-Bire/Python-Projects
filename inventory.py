
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
class Inventory:
    def __init__(self):
        self.products: list[Product] = []
    def add_product(self) -> None:
        name = input("Enter product name: ")

        if self.get_product(name) is not None:
            print("Product already exists.")
            return

        try:
            price = float(input("Enter product price: "))
            if price < 0:
                print("Price cannot be negative.")
                return

            quantity = int(input("Enter product quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:
            print("Invalid input. Please enter correct values.")
            return

        # Create Product object
        product = Product(name, price, quantity)

        # Add to list
        self.products.append(product)
        print(f"Product '{name}' added successfully.")
    def remove_product(self, product_name: str) -> None:
        if self.get_product(product_name) is None:
            print("Product not found.")
            return
        self.products = [product for product in self.products if product.name != product_name]
        print(f"Product '{product_name}' removed successfully.")
    def update_product(self, product_name: str, price: float | None = None, quantity: int | None = None) -> None:
        for product in self.products:
            if product.name == product_name:
                if price is not None:
                    product.price = price
                if quantity is not None:
                    product.quantity = quantity
                break
    def get_product(self, product_name: str) -> Product | None:
        for product in self.products:
            if product.name == product_name:
                return product
        return None
    def list_products(self) -> None:
        for product in self.products:
            if product.quantity > 0:
                print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            print("No products in inventory.")
          
    def total_value(self) -> float:
        return sum(product.price * product.quantity for product in self.products)
    def main(self) -> None:
        while True:
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Update Product")
            print("4. List Products")
            print("5. Total Inventory Value")
            print("6. Exit")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.add_product()
                case "2":
                    product_name = input("Enter product name to remove: ")
                    self.remove_product(product_name)
                case "3":
                    product_name = input("Enter product name to update: ")
                    price_input = input("Enter new price (leave blank to keep current): ")
                    quantity_input = input("Enter new quantity (leave blank to keep current): ")
                    price = float(price_input) if price_input else None
                    quantity = int(quantity_input) if quantity_input else None
                    self.update_product(product_name, price, quantity)
                case "4":
                    self.list_products()
                case "5":
                    print(f"Total Inventory Value: {self.total_value()}")
                case "6":
                    print("Exiting Inventory Management System.")
                    break
                case _:
                    print("Invalid choice. Please try again.")
if __name__ == "__main__":
    inventory = Inventory()
    inventory.main()
