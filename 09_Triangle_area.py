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

a = int(input('Enter First side'))
b = int(input('Enter second side'))
c = int(input('Enter Third side'))

# Caculate the area
area = a + b + c/2

# Calculate the perimeter
perimeter = a + b + c

print("\n Area of your Triangle is: %.2f" %area)
print(" Perimeter of your Triangle is: %2f" %perimeter)
