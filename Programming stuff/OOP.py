class employees:

    bonus = 0.2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay_method = pay
        self.pay = "$" + str(self.pay_method)#playing around here
        self.fullname = first + " " + last
        self.email = first + "." + last + "@company.com"

    def raise_pay(self, raise_flat, raise_percentage):
        self.pay_method += raise_flat
        self.pay_method *= 1 + raise_percentage

    def cut_pay(self, cut_flat, cut_percentage):
        self.pay_method -= cut_flat
        self.pay_method *= 1 - cut_percentage

    def emp_summary(self):
        print(self.fullname)
        print(self.email)
        print(self.pay)

class executives(employees):

    def __init__(self, first, last, pay, position, subordinates = None):
        super().__init__(first, last, pay)
        self.position = position
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

    def emp_summary(self):
        super().emp_summary()
        print(self.position)

        

james = executives("James", "Mak", 1000000, "CEO", [])
bob = executives("Bob", "Bobby", 700000, "CFO", [])
jim = executives("Jim", "Jimmy", 700000, "COO", [])

    
class managers(executives):
    def __init__(self, first, last, pay, position, superior):
        super().__init__(first, last, pay, position)
        self.superior = superior
        if superior == "James Mak":
            james.subordinates.append(self.fullname)
        elif superior == "Bob Bobby":
            bob.subordinates.append(self.fullname)
        elif superior == "Jim Jimmy":
            jim.subordinates.append(self.fullname)
            
            
Jen = managers("Jen", "Jenny", 500000, "General Manager", james.fullname)
Ben = managers("Ben", "Benny", 250000, "Accounts Manager", bob.fullname)
Kim = managers("Kim", "Kimmy", 250000, "Sales Manager", jim.fullname)










