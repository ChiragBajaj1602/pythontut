x=2
print(x==2,x==3,x>3)
name="john"
age=23
if name=="john" and age==23:
    print("your name is %s and your age is %s"%(name,age))
if name == "john" or name=="Rick":
    print("your name is either john or rick")
x=2
if x==2:
    print("x equals to 2")
else:
    print("x does not equal to 2")
x=[1,2,3]
y=[1,2,3]
if x is y:
    print("true")
else:
    print("false")
print(x==y)
print(not True)
print(not False)
# excercise for the conditional statements
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")