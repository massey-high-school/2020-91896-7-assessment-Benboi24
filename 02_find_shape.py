
# Not Blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response

# Main Routine goes here

# Iterates through string...

# ask user for string
shape_name=input()

print("Circle")
print("Triangle")
print("Square")
print("Rectangle")

shape_name = input("What is the shape name? ")

error = "Your shape name has numbers in it."
has_errors = ""

# look at each character in string and if it's a number, complain
for letter in shape_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# give user feedback...
if has_errors != "yes":
    print("you are OK")

print( "You have selected {}". format(shape_name))

