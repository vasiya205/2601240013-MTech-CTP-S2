from abc import ABC, abstractmethod


class Account(ABC):

  def __init__(self, account_number: str, balance: float):
    self.account_number = account_number
    self.balance = balance

  @abstractmethod
  def deposit(self, amount: float) -> None:
    pass

  @abstractmethod
  def withdraw(self, amount: float) -> None:
    pass


class SavingsAccount(Account):

  def deposit(self, amount: float) -> None:
    self.balance += amount

  def withdraw(self, amount: float) -> None:
    if amount <= self.balance:
      self.balance -= amount
    else:
      raise ValueError("Insufficient balance")


# Test Code
acc = SavingsAccount("ACC123", 1000.0)
acc.deposit(500.0)
acc.withdraw(200.0)
print(f"Account: {acc.account_number} | Final Balance: {acc.balance}")
