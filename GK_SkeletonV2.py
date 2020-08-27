# Welcome to The Area Perimeter Calculator

# ***** Functions ***** 

# Num Check
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

# Not Blank goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response

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

# Main Routine Starts Here
calculation_history = []

keep_going = ""
while keep_going == "":

  calcuation_row = []

  shape_name = string_checker("What is the shape name? ", ["xxx", "square", "circle", "triangle", "rectangle"])

  if shape_name.lower() == "xxx":
    break

  units = not_blank("What is your measurement? ")

  # calculations for each shape

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

  elif shape_name == "square":
      height = num_check("What is your side length?")

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
      base = num_check("What is your base?")

      # Area of a Rectangle
      # noinspection PyUnboundLocalVariable
      area = height * base
      perimeter = 2 * (height * base)

      # Print statements
      print("The area of your rectangle is {}".format(area))
      print("The perimeter of your rectangle is {}".format(perimeter))

  # Triangle
  elif shape_name == "triangle":
      # print(input)

      question = input("Do you have all the sides? ")
      # String Checker

      def string_checker(question, to_check,):
          valid = False
          while not valid:

              response = input(question).lower()

              if response in to_check:
                  return response

              else:
                  for item in to_check:
                      # checks if response is the first letter of an item in the list
                      if response == [0]:
                          # note: returns the entire response rather than just the first letter
                          return item

      if input == "yes":
          height = num_check("What is side A?")
          base = num_check("What is side B?")
          c = num_check("What is side C")

          # Calculate s
          s = (height + base + c) / 2

          # Calculate the area using herons rule
          area = (s * (s - height) * (s - base) * (s - c) ** .5)

          # Calculate the perimeter
          perimeter = height + base + c

      elif input in ["no", "n"]:

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


  calcuation_row.append(shape_name)
  calcuation_row.append(area)
  calcuation_row.append(perimeter)

  calculation_history.append(calcuation_row)



for item in calculation_history:
  print("{}: Area:{} {}^2 Perimeter: {} {}".format(item[0], item[1], units, item[2], units,))
