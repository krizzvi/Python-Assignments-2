import json

catalog = {"Laptop": 1000, "Phone": 600, "Headphones": 100}
cart = {}

def browse():
    print("\n--- Products ---")
    for item, price in catalog.items():
        print(f"{item}: ${price}")

def add_to_cart():
    item = input("Item to add: ")
    if item in catalog:
        qty = int(input("Quantity: "))
        cart[item] = cart.get(item, 0) + qty
        print("Item added.")
    else:
        print("Not found.")

def checkout():
    total = sum(catalog[i] * q for i, q in cart.items())
    print("Invoice:")
    for item, qty in cart.items():
        print(f"{item} x {qty} = ${catalog[item]*qty}")
    print(f"Total: ${total}")
    cart.clear()

def main():
    while True:
        print("\n--- E-Commerce ---")
        print("1. Browse")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            browse()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            checkout()
        elif choice == '4':
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()