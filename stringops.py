# anything that is passed in double quotes
bstring="world"
astring = "!Hello World"
print(len(astring))
print(astring.index('o'))
print(astring.count('l'))
print(astring[3:8])
# implementing a jump of a character
print(astring[3:8:2])
print(astring[-1:4:-2])
print(astring[::-1])
astring="Hello.World"
print(astring.upper())
print(astring.lower())
print(astring.capitalize())
astring="Hello world"
print(astring.startswith('Hello'))
print(astring.endswith('random'))
astring="Hello world"
afewords=astring.split(" ")
print(afewords)
# excercise
s = "Strb dbnana bnvbbome"
print("Length of s = %d" % len(s))
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[:5]) 
print("The next five characters are '%s'" % s[5:10]) 
print("The thirteenth character is '%s'" % s[12]) 
print("The characters with odd index are '%s'" %s[1::2]) 
print("The last five characters are '%s'" % s[-5:]) 
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
print("Split the words of the string: %s" % s.split(" "))