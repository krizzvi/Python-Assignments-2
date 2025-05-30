import json
from datetime import datetime

cars = {"Sedan": True, "SUV": True, "Hatchback": True}
rental_history = []

def list_cars():
    print("\n--- Available Cars ---")
    for car, available in cars.items():
        if available:
            print(car)

def book_car():
    list_cars()
    choice = input("Choose car: ")
    if cars.get(choice):
        cars[choice] = False
        start = datetime.now()
        rental_history.append({"car": choice, "start": str(start), "end": None})
        print(f"{choice} booked.")
    else:
        print("Car unavailable.")

def return_car():
    car = input("Enter car to return: ")
    for entry in rental_history:
        if entry["car"] == car and entry["end"] is None:
            entry["end"] = str(datetime.now())
            cars[car] = True
            print(f"{car} returned.")
            return
    print("Car not found or already returned.")

def view_history():
    for r in rental_history:
        print(r)

def main():
    while True:
        print("\n--- Car Rental System ---")
        print("1. List Cars")
        print("2. Book Car")
        print("3. Return Car")
        print("4. Rental History")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            list_cars()
        elif choice == '2':
            book_car()
        elif choice == '3':
            return_car()
        elif choice == '4':
            view_history()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()