mylist=[]
mylist.append(10)
mylist.append(11)
mylist.append(12)
print(mylist[0],mylist[1],mylist[2],sep=",")
for x in mylist:
    print(x)
# to raise an error by accessing an element that is not present in the list
print(mylist[10])
# excercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
mylist=[9,8,65]
print(mylist.sort())

strings.append("hello")
strings.append("world")

second_name = names[1]
# acces the second name at index 1 name : Eric
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
