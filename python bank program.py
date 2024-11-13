def show_balance(balance):
    print(f"Current balance: {balance}")


def deposit():
    amount = int(input("Deposit the amount to the bank: "))
    if amount < 0:
        print("The amount can't be negative")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = int(input("Withdraw the amount: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("The amount must be greater than zero")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:

        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        print("4. Show balance")

        choice = input("Choose your option (1-4): ")

        if choice == "1":
            balance += deposit()
        elif choice == "2":
            balance -= withdraw(balance)
        elif choice == "3":
            is_running = False
        elif choice == "4":
            show_balance(balance)
        else:
            print("Invalid choice, please choose a valid option (1-4).")

    print("Thank you!")


main()
