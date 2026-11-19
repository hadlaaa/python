class BankAccount:
    def __init__(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print("Name         :", self.name)
        print("Account No   :", self.acc_no)
        print("Account Type :", self.acc_type)
        print("Balance      :", self.balance)


name = input("Enter depositor name: ")
acc_no = input("Enter account number: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))
acc = BankAccount(name, acc_no, acc_type, balance)

while True:
    print("\n1.Deposit 2.Withdraw 3.Display 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        acc.deposit(float(input("Amount to deposit: ")))
    elif ch == 2:
        acc.withdraw(float(input("Amount to withdraw: ")))
    elif ch == 3:
        acc.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
