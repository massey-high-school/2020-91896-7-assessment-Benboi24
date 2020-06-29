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

# Main Rountine goes here
# Fiding area of a Rectangle

width = float(input('Please enter the widith of your Circle: '))
height = float(input('Please enter the height of your Circle: '))

# Caculate the area
area = 3.14 * r **2

# Calculate the perimeter
perimeter = 2 * 3.14 * r

print("\n Area of your Circle is: %.2f" %area)
print(" Perimeter of your Circle is: %2f" %perimeter)
