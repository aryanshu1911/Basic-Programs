def show_balance(balance):
    print(f"Balance: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be deposited: "))
    if amount < 0:
        print("Please enter a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount < 0:
        print("Please enter a valid amount")
        return 0
    elif amount > balance:
        print("Insufficient Balance!")
        return 0
    else:
        return amount

balance = 0
is_running = True



while is_running:
    print("\nWelcome to JSX Bank")
    print("1. Show Balance\n2. Deposit\n3. Withdrawal\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        withdrawal_amount = withdraw(balance)
        if withdrawal_amount > 0:
            balance -= withdrawal_amount
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

print("\nThank you for banking with us! Have a great day!")
