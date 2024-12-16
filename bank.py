import os

FILE_NAME = "accounts.txt"

def main():
    while True:
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Balance Inquiry")
        print("5. Update Account Details")
        print("6. Delete Account")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            balance_inquiry()
        elif choice == 5:
            update_account()
        elif choice == 6:
            delete_account()
        elif choice == 7:
            print("Thank you for using the Bank Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def create_account():
    name = input("Enter Name: ")
    account_number = input("Enter Account Number: ")
    age = input("Enter Age: ")
    balance = input("Enter Initial Balance: ")

    record = f"{name},{account_number},{age},{balance}\n"

    try:
        with open(FILE_NAME, "a") as file:
            file.write(record)
        print("Account created successfully!")
    except Exception as e:
        print(f"Error creating account: {e}")

def deposit_money():
    account_number = input("Enter Account Number: ")
    try:
        amount = float(input("Enter Deposit Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    accounts = read_accounts()
    found = False

    try:
        with open(FILE_NAME, "w") as file:
            for account in accounts:
                details = account.strip().split(",")
                if details[1] == account_number:
                    balance = float(details[3]) + amount
                    file.write(f"{details[0]},{details[1]},{details[2]},{balance}\n")
                    found = True
                else:
                    file.write(account)
            if found:
                print("Deposit successful!")
            else:
                print("Account not found.")
    except Exception as e:
        print(f"Error processing deposit: {e}")

def withdraw_money():
    account_number = input("Enter Account Number: ")
    try:
        amount = float(input("Enter Withdrawal Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    accounts = read_accounts()
    found = False

    try:
        with open(FILE_NAME, "w") as file:
            for account in accounts:
                details = account.strip().split(",")
                if details[1] == account_number:
                    balance = float(details[3])
                    if balance - amount >= 1000:
                        balance -= amount
                        file.write(f"{details[0]},{details[1]},{details[2]},{balance}\n")
                        found = True
                    else:
                        print("Insufficient balance. Minimum balance of ₹1000 must be maintained.")
                        file.write(account)
                else:
                    file.write(account)
            if found:
                print("Withdrawal successful!")
            else:
                print("Account not found.")
    except Exception as e:
        print(f"Error processing withdrawal: {e}")

def balance_inquiry():
    account_number = input("Enter Account Number: ")
    accounts = read_accounts()

    for account in accounts:
        details = account.strip().split(",")
        if details[1] == account_number:
            print(f"Current Balance: {details[3]}")
            return

    print("Account not found.")

def update_account():
    account_number = input("Enter Account Number: ")
    new_name = input("Enter New Name: ")
    new_age = input("Enter New Age: ")

    accounts = read_accounts()
    found = False

    try:
        with open(FILE_NAME, "w") as file:
            for account in accounts:
                details = account.strip().split(",")
                if details[1] == account_number:
                    file.write(f"{new_name},{details[1]},{new_age},{details[3]}\n")
                    found = True
                else:
                    file.write(account)
            if found:
                print("Account updated successfully!")
            else:
                print("Account not found.")
    except Exception as e:
        print(f"Error updating account: {e}")

def delete_account():
    account_number = input("Enter Account Number: ")
    accounts = read_accounts()
    found = False

    try:
        with open(FILE_NAME, "w") as file:
            for account in accounts:
                details = account.strip().split(",")
                if details[1] == account_number:
                    found = True
                else:
                    file.write(account)
            if found:
                print("Account deleted successfully!")
            else:
                print("Account not found.")
    except Exception as e:
        print(f"Error deleting account: {e}")

def read_accounts():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return file.readlines()

if __name__ == "__main__":
    main()
