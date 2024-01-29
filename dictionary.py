phonebook={}
phonebook["John"]=9787877676
phonebook["Jack"]=9383772643
phonebook["jill"]=7387638783
print(phonebook)
for name , number in phonebook.items():
    print("Phone number of %s is %d"%(name,number))
del phonebook["John"]
print(phonebook["jill"])
phonebook.pop("Jack")
phonebook={'John': 9787877676, 'Jack': 9383772643, 'Jill': 7387638783}
phonebook["Jake"]=938273443
del phonebook["Jill"]
if "Jake" in phonebook:
    print("Jake is listed in phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook")


