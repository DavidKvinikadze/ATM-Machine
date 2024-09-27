def validate_card(card_number, customer_card_numbers):
    return card_number in customer_card_numbers

def select_currency_type(balance, currency):
    if currency.lower() == "euro":
        balance *= 0.95
    elif currency.lower() == "pound":
        balance *= 0.82
    return balance

def deposit(balance, deposit_amount):
    balance += deposit_amount
    print("Deposit has been made successfully!")
    print(f"New balance: ${balance:.2f}")
    return balance

def withdraw(balance, withdrawal_amount, currency):
    while withdrawal_amount > balance:
        print("You don't have enough money.")
        withdrawal_amount = float(input("Enter a valid withdrawal amount: "))
    balance -= withdrawal_amount
    print("Withdrawal was successful!")
    print(f"Remaining balance: ${balance:.2f} {currency}")
    return balance

def main():
    # Initialize 3 customer information
    customer_card_numbers = ["1111111111111111", "2222222222222222", "3333333333333333"]
    customer_pins = ["1234", "2345", "3456"]
    customer_balances = [800, 1200, 1500]

    check = "yes"  # Initialize check variable
    card_number = None
    pin = None
    current_customer_index = None

    while check.lower() == "yes":
        if not card_number or not pin:
            # Service #1 - Card Validation
            card_number = input("Enter your card number: ")
            if validate_card(card_number, customer_card_numbers):
                # Valid card number, ask for the PIN
                current_customer_index = customer_card_numbers.index(card_number)
                pin = input("Enter your PIN: ")
                if pin != customer_pins[current_customer_index]:
                    print("Invalid PIN. Please try again.")
                    card_number = None
                    pin = None
                    continue
            else:
                print("Invalid card number. Please try again.")
                card_number = None
                pin = None
                continue

        # Service #2 - Choosing Currency
        currency = input("Choose your currency (Euro, US dollar, or Pound): ")
        customer_balances[current_customer_index] = select_currency_type(customer_balances[current_customer_index], currency)
        print(f"Your available balance: ${customer_balances[current_customer_index]:.2f} {currency}")

        # Service #3 & 4 Ask for deposit or withdrawal
        transaction = input("Do you want to make a deposit or withdrawal? (deposit/withdraw/no): ")
        if transaction.lower() == "deposit":
            deposit_amount = float(input("Enter the deposit amount: "))
            customer_balances[current_customer_index] = deposit(customer_balances[current_customer_index], deposit_amount)
        elif transaction.lower() == "withdraw":
            withdrawal_amount = float(input("Enter the withdrawal amount: "))
            customer_balances[current_customer_index] = withdraw(customer_balances[current_customer_index], withdrawal_amount, currency)

        check = input("Does another user want to do the operation? (yes or no): ")
        if check.lower() == "yes":
            # Reset for next customer
            card_number = None
            pin = None
        else:
            print("Thank you for using the ATM. Have a nice day!")

if __name__ == "__main__":
    main()