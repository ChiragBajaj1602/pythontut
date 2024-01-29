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