#Nested Function
#Store inner function to the outer function

def greet(name):
    # inner function
    def display_name():
        print("Hi", name)
    # call inner function
    display_name()
# call outer function
greet("Raja")
# Output: Hi Raja


def greet():
    # variable defined outside the inner function
    name = "Raja"
    # return a nested anonymous function
    return lambda: "Hi " + name
# call the outer function
message = greet()
# call the inner function
print(message())
# Output: Hi John

