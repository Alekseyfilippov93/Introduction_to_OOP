class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __str__(self):
        return f"{self.first} {self.last} ({self.pay})"

    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee("Ivan", "Ivanov", 5000)
emp2 = Employee("Petr", "Petrivicn", 3000)

sum_pay = emp1 + emp2
print(sum_pay)
