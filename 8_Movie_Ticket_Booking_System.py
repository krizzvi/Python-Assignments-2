seats = [[0 for _ in range(5)] for _ in range(5)]
movies = ["Spiderman", "Batman", "Inception"]

def view_movies():
    for i, m in enumerate(movies):
        print(f"{i+1}. {m}")

def book_ticket():
    view_movies()
    movie = input("Choose movie: ")
    row = int(input("Row (0-4): "))
    col = int(input("Col (0-4): "))
    if seats[row][col] == 0:
        seats[row][col] = 1
        print("Seat booked.")
    else:
        print("Seat taken.")

def print_receipt():
    print("Thanks for booking. Show this receipt at the theater.")

def main():
    while True:
        print("\n--- Movie Booking ---")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Print Receipt")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            view_movies()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            print_receipt()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()