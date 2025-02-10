# Python Banking Program

def show_balance(balance):
    print(f"Your balance is Rs {balance:.2f}")

def deposit():
    try:
        amount = float(input("Enter your deposit amount: "))
        if amount < 0:
            print("You cannot deposit negative amounts")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0

def withdraw(balance):
    try:
        amount = float(input("Enter your withdraw amount: "))
        if amount > balance:
            print("You cannot withdraw more than your balance")
            return 0
        elif amount < 0:
            print("You must withdraw an amount greater than 0")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0

def main():
    balance = 0
    is_running = True
    while is_running:
        print("****************")
        print("Banking Program ")
        print("****************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("****************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice")

    print("Thank You! Have a nice day!")

if __name__ == "__main__":
    main()
