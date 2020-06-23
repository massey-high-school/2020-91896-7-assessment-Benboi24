# Component 5 Dimension input
# Ask user what their shape is
# Ask for dimensions
# Print a list for the dimension and shape name

# Not blank function goes here
def not_blank(question):
    error = "This is invalid, please enter your shape name."


    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # look at each character in string and if it's a letter, complain
        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"
                break

        if response == "":
             continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# Ask for name of shape

shape_name = "What shape will you be making? "

# look at each character in string and if it's a number, complain
for letter in shape_name:

    if letter.isdigit():
        print(error)
        has_errors = "yes"
        break

print= "you are making {} ".format(input)

# Ask for dimensions

print= "What is side A?"

# look at each character in string and if it's a letter, complain
for letter in shape_name:
        if letter.isdigit() == True:
            has_errors = "yes"
            break

