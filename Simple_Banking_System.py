from datetime import datetime
import itertools

# -------------------------
# Transaction Class
# -------------------------
class Transaction:
    _id_counter = itertools.count(1)

    def __init__(self, account_number, amount, ttype):
        self.transaction_id = f"T{next(Transaction._id_counter):05d}"
        self.account_number = account_number
        self.amount = amount
        self.type = ttype   # "deposit" or "withdrawal"
        self.date = datetime.now()

    def display_transaction(self):
        return (f"{self.transaction_id} | {self.type.title():10s} | "
                f"Account: {self.account_number} | "
                f"Amount: {self.amount:.2f} | "
                f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")


# -------------------------
# BankAccount Class
# -------------------------
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []   # store Transaction objects

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        txn = Transaction(self.account_number, amount, "deposit")
        self.transactions.append(txn)

        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        return txn

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        txn = Transaction(self.account_number, amount, "withdrawal")
        self.transactions.append(txn)

        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        return txn

    def display_balance(self):
        return (f"Account: {self.account_number} | "
                f"Holder: {self.account_holder} | "
                f"Balance: {self.balance:.2f}")

    def display_statement(self):
        if not self.transactions:
            return "No transactions yet."

        lines = [f"Statement for {self.account_holder} (Account {self.account_number}):"]
        for txn in self.transactions:
            lines.append(txn.display_transaction())

        return "\n".join(lines)


# -------------------------
# Test the System
# -------------------------
if __name__ == "__main__":
    # Create accounts
    acc1 = BankAccount("00012345", "Alice Johnson", 500.0)
    acc2 = BankAccount("00054321", "Bob Singh", 1000.0)

    print(acc1.display_balance())
    print(acc2.display_balance())
    print()

    # Perform transactions
    acc1.deposit(250)
    try:
        acc1.withdraw(900)   # this will fail
    except ValueError as e:
        print("Withdrawal failed:", e)

    acc1.withdraw(200)
    acc2.deposit(1500)
    acc2.withdraw(300)

    print("\n" + acc1.display_statement())
    print("\n" + acc2.display_statement())
