class Account:

    def __init__(self, name, account_number, balance):
        self._name = name
        self._account_number = account_number
        self._balance = balance

    # getters and setters
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        print(type(self))
        return f"The balance of the account {self._account_number} ({self._name}) is {self._balance}"

    # withdraw method, raises
    def withdraw(self, amount):
        if (self._balance < amount):
            raise ValueError("insufficient Funds Available")
        else:
            self._balance = self._balance - amount
            print(f"You have withdrawn {amount} - remaning balance is {self._balance}")




class Premier(Account):
    premier_overdraft = 500


    def withdraw(self, amount):
        if (self._balance + Premier.premier_overdraft< amount):
            raise ValueError("insufficient Funds Available")
        else:
            self._balance = self._balance - amount
            print(f"You have withdrawn {amount} - remaning balance is {self._balance}")

    def monthly(self):
        self._balance = self._balance - 10
        print(f"You have withdrawn £10 {self._balance} left")
        print(Premier.monthly(self))



premier1 = Premier("Mick", "A2", 1)
#premier1.withdraw(2500)
#print(premier1)


p = Premier(Account, 1, 1)
p.monthly()


account1 = Account("Fouad", "A1" , 10.99)
#print(account1.get_balance())
#account1.withdraw(9)
#print(account1)

# 2 lines of code that will withdraw £10 from premier accounts

"""
# Multi-level inheritance
class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salery = salary

    def show_salary(self):
        print("Salary from Employee is", self._salery)

class Manager(Employee):
    def show_salary(self):
        print("Salary from Employee is", self._salery)


p = Person("Fouad", 20)

e = Employee("Mohammed", 30, 100)

m = Manager("Ahmed", 50, 1500)

m.show_salary()"! """
