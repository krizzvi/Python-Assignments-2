balance = 1000
pin = "1234"

def login():
    entered = input("Enter PIN: ")
    return entered == pin

def atm_menu():
    global balance
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        c = input("Choose: ")
        if c == '1':
            print(f"Balance: ${balance}")
        elif c == '2':
            amt = float(input("Amount: "))
            balance += amt
        elif c == '3':
            amt = float(input("Amount: "))
            if amt <= balance:
                balance -= amt
            else:
                print("Insufficient funds.")
        elif c == '4':
            break

def main():
    if login():
        atm_menu()
    else:
        print("Incorrect PIN")

if __name__ == "__main__":
    main()