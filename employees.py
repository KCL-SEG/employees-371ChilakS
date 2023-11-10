"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary = 0, hourlyWage = 0, noOfHoursWorked = 0, payPerCommision = 0,noOfContracts = 0, bonus = 0):
        self.name = name
        self.monthlySalary = monthlySalary
        self.hourlyWage = hourlyWage
        self.noOfHoursWorked = noOfHoursWorked
        self.payPerCommision = payPerCommision
        self.noOfContracts = noOfContracts
        self.bonus = bonus
        #self.get_pay = None

    def get_pay(self):
        totalPay = 0
        if self.monthlySalary:
            totalPay += self.monthlySalary
        elif self.hourlyWage and self.noOfHoursWorked:
            totalPay += self.hourlyWage * self.noOfHoursWorked

        if self.payPerCommision and self.noOfContracts:
            totalPay += self.payPerCommision * self.noOfContracts
        elif self.bonus:
            totalPay += self.bonus
        
        return totalPay


    def __str__(self):
        description = self.name

        if self.monthlySalary:
            description += f' works on a monthly salary of {self.monthlySalary}' 
        elif self.hourlyWage and self.noOfHoursWorked:
            description += f' works on a contract of {self.noOfHoursWorked} hours at {self.hourlyWage}/hour'

        if self.payPerCommision and self.noOfContracts:
            description += f' and recieves a commission of {self.noOfContracts} contract(s) at {self.payPerCommision}/contract' 
        elif self.bonus:
            description += f' and recieves a bonus commission of {self.bonus}' 

        return description + f'.Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',monthlySalary= 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',hourlyWage = 25,noOfHoursWorked = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthlySalary= 3000,payPerCommision = 200,noOfContracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',hourlyWage = 25,noOfHoursWorked = 150,payPerCommision = 220,noOfContracts = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthlySalary= 2000, bonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',hourlyWage = 30,noOfHoursWorked = 120, bonus = 600)



print(f'{str(billie)}   {billie.get_pay()}')
print(f'{str(charlie)}   {charlie.get_pay()}')
print(f'{str(renee)}   {renee.get_pay()}')
print(f'{str(jan)}   {jan.get_pay()}')
print(f'{str(robbie)}   {robbie.get_pay()}')
print(f'{str(ariel)}   {ariel.get_pay()}')