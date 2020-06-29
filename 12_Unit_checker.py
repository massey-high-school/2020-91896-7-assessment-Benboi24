
# Get's measurement and check its is not blank

# Checks for no numbers
# Iterates through string...

# ask user for string
measurment_name = input("What is your measurement? ")

error = "Your measurment has numbers in it."
has_errors = ""

# look at each character in string and if it's a number, complain
for letter in measurment_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

# give user feedback...
if has_errors != "yes":
    print("you are OK")

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

recipe_name = not_blank("What is your measurement? ")

print( "You have chosen {}". format(recipe_name))