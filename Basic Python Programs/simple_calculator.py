# Program to create a Simple Calculator...

# Defining functions for each operation
def sum (a, b):
        return a + b

def difference (a, b):
        return a - b

def product (a, b):
        return a * b

def division (a, b):
        if b == 0:
            print("Division by 0 not possible")
        else:
             return a / b
        
# Take input from the users
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1.Sum\n2.Difference\n3.Product\n4.Division\n5.Exit")
operation = input("Enter the operation:")

# Execute program by calling functions inside print() statement
if operation == "1":
    print (f"Sum of {a} and {b} is", sum(a, b))
elif operation == '2':
    print (f"Difference of {a} and {b} is", difference(a, b))
elif operation == '3':
    print (f"Product of {a} and {b} is", product(a, b))
elif operation == '4':
    print (f"Division of {a} with {b} is", division(a, b))
elif operation == '5':
    exit()
else:
    print ("Invalid operation")

