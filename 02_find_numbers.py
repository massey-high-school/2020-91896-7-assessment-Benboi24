# Functions go here
def num_check(type, question, lowest):

  # Set up error message so that it specifies either 'an integer' or 'a number' depending on the 'type'.
  if type == int:
    error_specific = "an integer"
  else:
    error_specific = "a number"

  error = "Please enter a shape \n".format(error_specific, lowest)

  valid = False
  while not valid:

    # Ask the question and check that the answer is valid
    try:
      response = type(input(question)

        return response
      else:
        print(error)

      except ValueError:
        print(error)

# **** Main Routine Goes Here

# Ask for number of items
num_items = num_check(int, "What shape will you be making"
                           "Please enter  a number below for your shape"
                           "1:Circle"
                           "2:Shape? ",)


print("you are making {} }".format(num_items,))

