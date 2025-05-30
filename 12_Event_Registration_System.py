from collections import deque

slots = 5
registered = []
waitlist = deque()

def register(name):
    if len(registered) < slots:
        registered.append(name)
        print(f"{name} registered.")
    else:
        waitlist.append(name)
        print(f"{name} added to waitlist.")

def show_lists():
    print("Registered:", registered)
    print("Waitlist:", list(waitlist))

def main():
    while True:
        print("\n1. Register\n2. Show List\n3. Exit")
        c = input("Choose: ")
        if c == '1':
            name = input("Enter name: ")
            register(name)
        elif c == '2':
            show_lists()
        elif c == '3':
            break

if __name__ == "__main__":
    main()