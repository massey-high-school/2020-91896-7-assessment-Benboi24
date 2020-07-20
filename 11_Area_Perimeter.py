# Welcome to The Area Perimeter Calculator

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

# looks at each character in string and if it's a number, complain
for letter in shape_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# give user feedback...
if has_errors != "yes":
    print("you are OK")

print("You have selected {}". format(shape_name))
# Asked what the name of the shape was

# Ask what the side a and b is
# Write formula so program can print correctly

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
# Finding area of a Rectangle

width = float(input('Please enter the widith of your rectangle: '))
height = float(input('Please enter the height of your rectangle: '))

# Calculate the area
area = width * height

# Calculate the perimeter
perimeter = 2 * (width + height)

print("\n Area of your rectangle is: %.2f" %area)
print(" Perimeter of your rectangle is: %2f" %perimeter)

# Ask what the width and height
# Write formula so program can print correctly


# Not Blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response

# Main Rountine goes here
# Fiding area of a Square
a = float(input('Please enter the widith of your Square: '))
b = float(input('Please enter the height of your Square: '))

# Calculate the area
area = a ** 2

# Calculate the perimeter
perimeter = 4 * a

print("\n Area of your square is: %.2f" %area)
print(" Perimeter of your square is: %2f" %perimeter)

# Ask what the side a, b and c is
# Write formula so program can print correctly


# Not Blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response

# Main Rountine goes here

a = int(input('Enter First side'))
b = int(input('Enter second side'))
c = int(input('Enter Third side'))

# Calculate the area
area = a * b/2

# Calculate the perimeter
perimeter = a + b + c

print("\n Area of your Triangle is: %.2f" %area)
print(" Perimeter of your Triangle is: %2f" %perimeter)


# Ask what the radius is
# Write formula so program can print correctly
# Use letters not width or length

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
# Finding area of a Circle
r = float(input('Please enter the radius: '))

# Calculate the area
area = 3.14 * r **2

# Calculate the perimeter
perimeter = 2 * 3.14 * r

print("\n Area of your Circle is: %.2f" %area)
print(" Perimeter of your Circle is: %2f" %perimeter)



