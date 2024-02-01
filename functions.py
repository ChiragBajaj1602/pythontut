def my_function():
    print("Hello from my function")
def my_function_with_args(username,greeting):
    print("Hello, %s,From My function!, I wish you %s"%(username,greeting))
my_function_with_args("Chirag","Hello")
def sum_two_numbers(a,b):
    return a+b
print(sum_two_numbers(10,10))
# added the return statements
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
def build_sentence(benefit):
    return benefit+" is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
def my_function(*kids):
    print(f"The most mischiveous child among all is {kids[2]}")
my_function("john","sturgis","sheldon")
def my_function_with(**kid):
    print("His Last name  is "+kid["lname"])
my_function_with(fname="sheldon",lname="cooper")
# passing a list as an argument
def trirecursion(k):
    if(k>0):
        result=k+trirecursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\n Recursion example results")
trirecursion(6)
# lamda functions 
x=lambda a:a+10
print(x(5))

# x recieves the value of the 
# lamda function
def myfunction(n):
    return lambda a:a*n
mytripler=myfunction(3)
result=mytripler(2)
print(result)
