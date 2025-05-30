import json
import time
import random

MENU = {
    "Pizza": 8.99,
    "Burger": 5.49,
    "Pasta": 7.99,
    "Salad": 4.99,
    "Soda": 1.99
}

orders = []

def browse_menu():
    print("\n--- MENU ---")
    for item, price in MENU.items():
        print(f"{item}: ${price}")

def place_order():
    browse_menu()
    order = {}
    while True:
        item = input("Enter item name to add to order (or type 'done'): ").title()
        if item.lower() == "done":
            break
        if item in MENU:
            qty = int(input(f"Enter quantity for {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not found. Try again.")
    if order:
        order_id = random.randint(1000, 9999)
        total = sum(MENU[item] * qty for item, qty in order.items())
        orders.append({"id": order_id, "order": order, "total": total, "status": "Preparing"})
        with open("orders.json", "w") as f:
            json.dump(orders, f)
        print(f"\nOrder placed! Order ID: {order_id}, Total: ${total:.2f}")

def track_order():
    try:
        order_id = int(input("Enter your Order ID: "))
        with open("orders.json", "r") as f:
            all_orders = json.load(f)
        for o in all_orders:
            if o["id"] == order_id:
                print(f"Order Status: {o['status']}")
                return
        print("Order ID not found.")
    except FileNotFoundError:
        print("No orders found.")

def generate_bill():
    try:
        with open("orders.json", "r") as f:
            all_orders = json.load(f)
        print("\n--- All Bills ---")
        for o in all_orders:
            print(f"Order ID: {o['id']}, Total: ${o['total']:.2f}")
    except FileNotFoundError:
        print("No orders found.")

def main():
    while True:
        print("\n--- Online Food Ordering System ---")
        print("1. Browse Menu")
        print("2. Place Order")
        print("3. Track Order")
        print("4. Generate Bills")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            browse_menu()
        elif choice == '2':
            place_order()
        elif choice == '3':
            track_order()
        elif choice == '4':
            generate_bill()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()