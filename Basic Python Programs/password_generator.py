# Program to create a Password Generator...


# importing string and random libraries
import string
import random

def main():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits
    special = string.punctuation

    pass_len = int(input("Enter the length of the password: "))

    # Create an empty list where all characters are to be stored
    s = []
    s.extend(upper)
    s.extend(lower)
    s.extend(digit)
    s.extend(special)

    # Shuffle the characters in the list s to randomize the password order
    random.shuffle(s)   
    password = ''.join(s[0:pass_len])
    print("Your password is: ", password)

# Run the program
if __name__ == '__main__':
    main()
    