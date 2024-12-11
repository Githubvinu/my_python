class salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self,name,age,salry):
        self.name = name
        self.age = age
        self.obj_salary = salry

    def total_salary(self):
        return self.obj_salary.annual_salary()

salry = salary(150000 , 100000)
emp = Employee('vinay', 25 , salry)
print(emp.total_salary())