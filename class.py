class Myclass:
    variable="blah"
    def function(self):
        print("this is a message inside the class.")
myobjectx=Myclass()
myobjectx.function()
class NumberHolder:
    def __init__(self,number):
        self.number=number
    def returnNumber(self):
        return self.number
var=NumberHolder(7)
print(var.returnNumber())
# excercise
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
car1=Vehicle()
car1.name='Fer'
car1.kind="Convertible"
car1.color='red'
car1.value=60000
car2=Vehicle()
car2.name='jump'
car2.kind="van"
car2.color='blue'
car2.value=10000
# test code
print(car1.description())
print(car2.description())
# practiced inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

   
x = Student("Mike", "Olsen")
x.printname()
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("welcome {self.firstname} {self.lastname} to the class of {}")

x = Student("Mike", "Olsen", 2019)
x.welcome()
