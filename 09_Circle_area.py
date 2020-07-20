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
width = float(input('Please enter the widith of your rectangle: '))
height = float(input('Please enter the height of your rectangle: '))

# Caculate the area
area = width * height

# Calculate the perimeter
perimeter = 2 * (width + height)

print("\n Area of your square is: %.2f" %area)
print(" Perimeter of your square is: %2f" %perimeter)

