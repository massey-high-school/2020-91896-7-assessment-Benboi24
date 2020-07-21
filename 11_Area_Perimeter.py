# Welcome to The Area Perimeter Calculator

# ***** Functions *****

# Number checking function (number must be a float that is more than 0)
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# String checking Function
def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks if response is the first letter of an item in the list
                if response == item[0]:
                    # note: returns the entire response rather than just the first letter
                    return item

        print("sorry that is not a valid response")

# Yes No Function

answer = None
while answer not in ("yes", "no"):
    answer = input("Enter yes or no: ")
    if answer == "yes":
        # Do this.
    elif answer == "no":
        # Do that.
    else:
    	print("Please enter yes or no.")

# *** Main Routine starts here ***

yes_no = ["yes", "no"]
rps = ["rock", "paper", "scissors"]

mood = string_checker("Are you happy? ", yes_no)
print(mood)

choose = string_checker("Choose: ", rps)
print(choose)


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

Circle = shape_name
if input(Circle):
    print("Okay")
Triangle = shape_name
if input(Triangle):
    print("Okay")
Square = shape_name
if input(Square):
    print("Okay")
Rectangle = shape_name
if input(Rectangle):
    print("Okay")

# Ask what the side a and b is
# Write formula so program can print correctly
# Main Routine goes here
# Finding area of a Rectangle

height = float(input('Please enter the height of your rectangle: '))
width = float(input('Please enter the width of your rectangle: '))
# Calculate the area
area = width * height

# Calculate the perimeter
perimeter = 2 * (width + height)

print("\n Area of your rectangle is: %.2f" %area)
print(" Perimeter of your rectangle is: %2f" %perimeter)

# Ask what the width and height
# Write formula so program can print correctly


# Main Routine goes here
# Finding area of a Square
a = float(input('Please enter the width of your Square: '))

# Calculate the area
area = a ** 2

# Calculate the perimeter
perimeter = 4 * a

print("\n Area of your square is: %.2f" %area)
print(" Perimeter of your square is: %2f" %perimeter)

# Ask what the side a, b and c is
# Write formula so program can print correctly

# Main Routine goes here

a = int(input('Please enter side a'))
base = int(input('Please enter Base '))
c = int(input('Please enter side c'))

# Calculate the area
area = a * base/2

# Calculate the perimeter
perimeter = a + base + c

print("\n Area of your Triangle is: %.2f" %area)
print(" Perimeter of your Triangle is: %2f" %perimeter)


# Ask what the radius is
# Write formula so program can print correctly
# Use letters not width or length


# Main Routine goes here
# Finding area of a Circle
r = float(input('Please enter the radius: '))

# Calculate the area
area = 3.14 * r **2

# Calculate the perimeter
perimeter = 2 * 3.14 * r

print("\n Area of your Circle is: %.2f" %area)
print(" Perimeter of your Circle is: %2f" %perimeter)



