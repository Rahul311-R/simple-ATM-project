 
accounts = {  
   "1234": {"pin": "1234", "balance": 1000, "history": []},  
   "5678": {"pin": "5678", "balance": 500, "history": []}  
}  
  
def account_balance_inquiry(account_number):  
  
   return accounts[account_number]["balance"]  
  
def cash_withdrawal(account_number, amount):  
 
   if amount > accounts[account_number]["balance"]:  
      print("Insufficient funds")  
   else:  
      accounts[account_number]["balance"] -= amount  
      accounts[account_number]["history"].append(f"Withdrew ${amount}")  
      print(f"Withdrew ${amount}. Remaining balance: ${accounts[account_number]['balance']}")  
  
def cash_deposit(account_number, amount):  
 
   accounts[account_number]["balance"] += amount  
   accounts[account_number]["history"].append(f"Deposited ${amount}")  
   print(f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}")  
  
def pin_change(account_number, new_pin):  
  
   accounts[account_number]["pin"] = new_pin  
   print("PIN changed successfully")  
  
def transaction_history(account_number):  
 
   return accounts[account_number]["history"]  
  
def main():  
   print("Welcome to the ATM Machine Simulation")  
   account_number = input("Enter your account number: ")  
   pin = input("Enter your PIN: ")  
  
   if account_number in accounts and accounts[account_number]["pin"] == pin:  
      print("Login successful")  
      while True:  
        print("1. Account Balance Inquiry")  
        print("2. Cash Withdrawal")  
        print("3. Cash Deposit")  
        print("4. PIN Change")  
        print("5. Transaction History")  
        print("6. Exit")  
        choice = input("Enter your choice: ")  
  
        if choice == "1":  
           print(f"Account balance: ${account_balance_inquiry(account_number)}")  
        elif choice == "2":  
           amount = int(input("Enter amount to withdraw: "))  
           cash_withdrawal(account_number, amount)  
        elif choice == "3":  
           amount = int(input("Enter amount to deposit: "))  
           cash_deposit(account_number, amount)  
        elif choice == "4":  
           new_pin = input("Enter new PIN: ")  
           pin_change(account_number, new_pin)  
        elif choice == "5":  
           print("Transaction history:")  
           for transaction in transaction_history(account_number):  
              print(transaction)  
        elif choice == "6":  
           print("Exiting...")  
           break  
        else:  
           print("Invalid choice. Please try again.")  
   else:  
      print("Invalid account number or PIN")  
  
if __name__ == "__main__":  
   main()
