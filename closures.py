def transmit_to_message(message):
    '''This is the enclosing function'''
    def data_transmitter():
        '''The nested function'''
        print(message)

    data_transmitter()

print(transmit_to_message("This is Good"))

# now using the non local keyword

def print_msg(number):
    def printer():
        '''Here we are using the non local keyword'''
        nonlocal number
        number = 111
        print(number)
    printer()
    print(number)

print_msg(4)
        
# how about we  return the function object rather that calling the function which is data_transmitter
def transmit_to_message1(message):
    '''This is the enclosing function'''
    def data_transmitter():
        ''' The nested function'''
        print(message)
    return  data_transmitter
print(transmit_to_message1("Hi how are you?"))
# it will print the python function object

# excercise 
def multiplier_of(n):
    def wrapper(number):
        return number*n
    return wrapper
multiplywith5 = multiplier_of(5)
print(multiplywith5(4))
