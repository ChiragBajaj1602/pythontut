num=7
print(num)
myfloat=7.0
print(myfloat)
# string can be written in two ways using single and double quotes
string1="hello"
string2='hello'
print(string1)
print(string2)
# double quotes allow to use the apostrophe like in words like : Don't
string3="Don't Worry"
print(string3)
# string concatenation
a="hello"
b="world"
c=a+" "+b
print(c)
a,b=3,4
print(a,b)
one=1
two=2
three="hello"
# as the data types are not same hence concatenation will not be performed
# print(one+two+three)
# performed an excercise where the instances are matched along with their values
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
