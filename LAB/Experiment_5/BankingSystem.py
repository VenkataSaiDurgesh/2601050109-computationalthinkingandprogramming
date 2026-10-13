from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        pass

    def show(self) -> None:
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    def withdraw(self, amount: int) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):

    def withdraw(self, amount: int) -> None:
        self.balance -= amount


s = SavingsAccount("Sravani", 5000)

s.deposit(1000)
s.withdraw(2000)
s.show()


c = CurrentAccount("Ravi", 5000)

c.deposit(1000)
c.withdraw(3000)
c.show()
