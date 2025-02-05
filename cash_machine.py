class Cashmachine:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []
    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: ${amount:.2f}")
            return f"You have deposited: ${amount:.2f}"
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}")
            return f"You have withdrawn: ${amount:.2f}"
    def view_transaction_history(self):
        return "\n".join(self.transactions)
        if not self.transactions:
            return "No transactions made yet."
            

def main():
    cash_machine = Cashmachine()
    while True:
        print("\nCash Machine")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Select an option 1-5: ")
        if choice == '1':
            print(cash_machine.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            print(cash_machine.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            print(cash_machine.withdraw(amount))
        elif choice == '4':
            print("Here is your transaction history:")
            print(cash_machine.view_transactions())
        elif choice == '5':
            print("Good bye from Cash Machine!")
            break
        else:
            print("Invalid. Try again.")

if __name__ == "__main__":
    main()

    
