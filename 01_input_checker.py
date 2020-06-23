# Iterates through string...

# ask user for string
recipe_name = input("Please chose a number between 1 and 4? ")

error = "Your response name has numbers in it."
has_errors = ""


# look at each character in string and if it's a letter, complain
for letter in recipe_name:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break


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

# give user feedback...
if has_errors != "yes":
    print("you are OK")