from abc import ABC, abstractmethod

class CreditCard:
     def __init__(self, number: int):
          self.number = number

class CreditProcess(ABC):
    @abstractmethod
    def credit_processment(self, amount: float) -> bool:
        pass

class CreditPayment(ABC):
    def credit_processment(self, amount: float) -> bool:
        print("Processing ", amount, "via Credit")
        return True

card = CreditCard(1234)
payment = CreditPayment()

print("Credit card: ", card.number)
success = payment.credit_processment(270.5)
print("Payment status: ", success)