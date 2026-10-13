1. Algorithm / Procedure
Create an abstract BankAccount class.
Create SavingsAccount and CurrentAccount as child classes.
Use inheritance to get common methods.
Use an abstract withdraw() method.
Deposit and withdraw money.
Display the balance.
2. Very Simple Python Code
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


s = SavingsAccount("Suma", 5000)

s.deposit(1000)
s.withdraw(2000)
s.show()


c = CurrentAccount("Tabu", 5000)

c.deposit(1000)
c.withdraw(3000)
c.show()
3. Input and Output
Output:

Name: Suma
Balance: 4000
Name: Tabu
Balance: 3000
4. Inference
The program demonstrates abstraction and inheritance using a simple banking system.

5. Analysis
BankAccount is the abstract parent class. SavingsAccount and CurrentAccount inherit from it and provide their own withdraw() method. Time complexity: O(1) and space complexity: O(1).
