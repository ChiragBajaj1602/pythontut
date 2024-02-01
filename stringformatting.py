name="John"
print("my name is %s"%name)
# to format a string with more than one varriables using tuples
name="John"
age=21
print("My name is %s and my age is %d"%(name,age))
mylists=[1,2,3]
print("A list: %s"%mylists)
# string formatiing can also be achieved by the concept called fstring
print(f"the string formating is done by {name}")
# using the format method
txt="for only {weight:.2f} the price is 45$"
print(txt.format(weight=90))
