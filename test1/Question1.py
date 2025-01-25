
#checks the balaance in the account
def check_balance(money_in_account):
    print(f"Balance in the account is: {money_in_account}")
    print()
#function for depositing the money in the acccout
def deposit_money(money_in_account):
    amount = int(input("Enter the amount to deposit: "))
    money_in_account += amount
    print(f"Amount of {amount} has been deposited")
    print()  
    return money_in_account
#function for withdrawing the money from the account
def withdraw_money(money_in_account):
    amount = int(input("Enter the amount to withdraw: "))
    if amount > money_in_account:
        print("Insufficient balance")
        print()
        return money_in_account
    money_in_account -= amount
    print(f"Amount of {amount} has been withdrawn")
    print()
    return money_in_account
#Main or Driver function
def main():
    money_in_account = 0
    print("Welcome to the ATM")
    print()
    print("Deposit some money to start using the ATM")
    while 1:
        print("1. Check Balance in the account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            check_balance(money_in_account)
        elif choice == 2:
            money_in_account = deposit_money(money_in_account)
            print(f"Balance in the account is: {money_in_account}")
        elif choice == 3:
            money_in_account = withdraw_money(money_in_account)
            print(f"Balance in the account is: {money_in_account}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
main()
