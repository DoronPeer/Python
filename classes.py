class Employee:

  raise_amt = 1.05
  alem = 0

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@gmail.com'

    Employee.alem += 1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def app_raise(self):
    self.pay = int(self.pay * self.raise_amt)
  
  def __repr__(self):
      return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
  
  def __str__(self):
      return '{} - {}'.format(self.fullname(), self.email)

  @classmethod
  def from_str(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or  day.weekday() == 6:
     return False
    return True
    

class Developer(Employee):
  raise_amt = 1.10
  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang   

class manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)
  
  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_emps(self):
    for emp in self.employees:
      print('-->', emp.fullname())


dev_1 = Developer('Doron', 'peer', 50000, 'lava')
emp_1 = Employee('jhon', 'deer', 60000)
emp_2 = Employee('Keren', 'cooper', 60000)
mgr_1 = manager('Sue', 'Smith', 90000, [dev_1])

#allow us to print the format in spaical method
print(emp_1.__repr__())
print(emp_1.__str__())

mgr_1.add_emp(emp_2)

mgr_1.print_emps()
print(mgr_1.first)
print(mgr_1.email)

print(dev_1.pay)
dev_1.app_raise()
print(dev_1.pay)

#import datetime
#my_date = datetime.date(2020, 9, 19)
#print(Employee.is_workday(my_date))

emp_str_1 = 'Jhon-deer-70000'
emp_str_2 = 'dor-ma-30000'
new_emp_1 = Employee.from_str(emp_str_1)
print(new_emp_1.first)

# the 2 ways are the same
print(Employee.fullname(emp_1))
print(emp_1.fullname())

print(Employee.alem)
print(emp_1.__dict__)
print(emp_1.pay)
Employee.app_raise(emp_1)
print(emp_1.pay)
print(Employee.raise_amt)
print(emp_1.raise_amt)

