# performing some bodmas operations
numbers=1+2*3/4.0
print(numbers)
# printing the remainder 
x=11
print(x%8)
# using ** to perform exponent operation
print(7**2,7**3)
# operators such as addiition to perform concatenation in string
a="hello"
b="world"
c=a+" "+b
print(c)
# python supports the multiplying operation to write a word multiple times
word="Hello"
print(word*9)
# + operator can be used to concatenate lists
list1=[1,3,5,7]
list2=[2,4,6,8]
print(list1+list2)
# just like the string the multiplication symbol can be used to multiply the lists
list3=[1,2,3]
print(list3*8)
# excercise
x = object()
y = object()
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")