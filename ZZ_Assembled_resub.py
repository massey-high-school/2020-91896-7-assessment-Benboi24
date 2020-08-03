# Welcome to The Area Perimeter Calculator
# Don't include units because there are to many instead run through not blank function.

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


# *** Main Routine starts here ***

# Instructions
def instructions():
    print("****** Welcome to the Fund Raising Calculator ******")

    first_time = input("\nHave you used this program before? ")

    if first_time == "yes":
        return ""

    print()
    print("***** Instructions ******")
    print()
    print("This program will ask you for...")
    print("- The name of the shape you want to chose")
    print("- It will ask for the height, base or other sides depending on shape")
    print()
    print("The program will print out the area and perimeter for the shape you chose.")
    print()


instructions()

# List within a list
# Abbreviations list

def unit_checker(raw_unit):

    unit_tocheck = raw_unit

    # Abbreviation lists
    miles = ["mile",]
    millimeters = ["mLs", "milli", "mm"]
    meters = ["M", "m", "meters"]
    centimeters = ["cm","centimeters", "Cm"]
    yards = ["y", "yards"]
    feet = ["ft,"]
    kilometers = ["km", "kilo", ]
    inches = ["inches", "inch"]

    if unit_tocheck == "":
        # print("You chose {}".format(unit_tocheck))
        return unit_checker
    elif unit_tocheck.lower() in miles:
        return "Miles"
    elif unit_tocheck == "T" or unit_tocheck.lower() in feet:
        return "feet"
    elif unit_tocheck.lower() in millimeters:
        return "Millimeters"
    elif unit_tocheck.lower() in meters:
        return "Meters"
    elif unit_tocheck.lower() in centimeters:
        return "Centimeters"
    elif unit_tocheck.lower() in yards:
        return "Yards"
    elif unit_tocheck.lower() in kilometers:
        return "Kilometers"
    elif unit_tocheck.lower() in inches:
        return "I"

# Get's measurement and check its is not blank

# Checks for no numbers
# Iterates through string...

# ask user for string
measurement_name = not_blank("What is your measurement? ")

# String Checker
yes_no = ["yes", "no"]
shapes = ["circle","triangle", "square", "rectangle"]

# Main Routine goes here

# Iterates through string...

# ask user for string
# Instructions

shape_name = string_checker("What is the shape name? ", shapes)

print("You have selected {}". format(shape_name))
# Asked what the name of the shape was

# If statements
# Circle
if shape_name == "circle":
    radius = num_check("What is the radius? ")

    # Area of a circle
    # noinspection PyUnboundLocalVariable
    area = 3.14 * radius ** 2
    perimeter = 2 * 3.14 * radius

    # Print Statements
    print("The area of your circle is {}". format(area))
    print('The perimeter of your circle is {}'.format(perimeter))

# Square
elif shape_name == "square":
    height = num_check("What is your height?")

    # Area of a Square
    # noinspection PyUnboundLocalVariable
    area = height ** 2
    perimeter = height * 4

    # Print Statements
    print("The area of your square is {}". format(area))
    print("The perimeter of your square is {}".format(perimeter))

# Rectangle
elif shape_name == "rectangle":
    height = num_check("What is your height?")
    base = "What is your base?"

    # Area of a Rectangle
    # noinspection PyUnboundLocalVariable
    area = height * base
    perimeter = 2 * (height * base)

    # Print statements
    print("The area of your rectangle is {}".format(area))
    print("The perimeter of your rectangle is {}".format(perimeter))

# Triangle
elif shape_name == "triangle":
    print(input)

    all_sides = input("Do you have all the sides? ")

    if all_sides in ["yes", "y"]:

        height = num_check("What is side A?")
        base = num_check("What is side B?")
        c = num_check("What is side C")

        # Calculate s
        s = (height + base + c) / 2

        # Calculate the area using herons rule
        area = (s * (s - height) * (s - base) * (s - c) ** 0.5)

        # Calculate the perimeter
        perimeter = height + base + c

    if all_sides in ["no", "n"]:

        height = num_check("What is the height?")
        base = num_check("What is the base?")

        # area using height and the base
        # noinspection PyUnboundLocalVariable
        area = 0.5 * height * base
        s = "n/a"

    # noinspection PyUnboundLocalVariable
    # Print Statements
    print("The area of your triangle is {}".format(area))
    print("The perimeter of your triangle is {}".format(perimeter))

# Output History
