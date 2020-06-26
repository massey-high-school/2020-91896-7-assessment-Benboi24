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
# Fiding area of a square
width = float(input('Please enter the widith of your Square: '))
height = float(input('Please enter the height of your Square: '))

# Caculate the area
area = height ** 2

# Calculate the perimeter
perimeter = 4 * height

print("\n Area of your square is: %.2f" %area)
print(" Perimeter of your square is: %2f" %perimeter)

