
balance = 10000 #Iitial balance
MIN_BALANCE = 500
transactions = []   # list to store transaction history

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(f"Current Balance: ₹{balance}")
        transactions.append(f"Checked balance: ₹{balance}")

    elif choice == 2:
        deposit = int(input("Enter amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print("Deposit successful!")
            print(f"Updated Balance: ₹{balance}")
            transactions.append(f"Deposited ₹{deposit} | Balance ₹{balance}")
        else:
            print("Invalid deposit amount!")

    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= 0:
            print("Invalid withdrawal amount!")

        elif balance - withdraw < MIN_BALANCE:
            print("Insufficient balance!")
            print(f"Minimum balance of ₹{MIN_BALANCE} must be maintained.")
            transactions.append(f"Failed withdrawal attempt of ₹{withdraw}")

        else:
            balance -= withdraw
            print("Withdrawal successful!")
            print(f"New Balance: ₹{balance}")
            transactions.append(f"Withdrew ₹{withdraw} | Balance ₹{balance}")

    elif choice == 4:
        print("\n--- Transaction History ---")
        if not transactions:
            print("No transactions yet.")
        else:
            for i, transaction in enumerate(transactions, start=1):
                print(f"{i}. {transaction}")

    elif choice == 5:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.")