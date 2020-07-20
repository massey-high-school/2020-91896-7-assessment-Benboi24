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
a = float(input('Please enter side a: '))

# Caculate the area
area = a ** 2

# Calculate the perimeter
perimeter = 4 * a

print("\n Area of your square is: %.2f" %area)
print(" Perimeter of your square is: %2f" %perimeter)

