# Functions

# Not Blank

#  Main routine starts here

calculation_history = []

keep_going = ""
while keep_going == "":

  calcuation_row = []

  shape = input("Shape? ")
  if shape.lower() == "xxx":
    break

  # calculations for each shape
  units = "cm"
  area = 3
  perimeter = 4

  calcuation_row.append(shape)
  calcuation_row.append(area)
  calcuation_row.append(perimeter)

  calculation_history.append(calcuation_row)



for item in calculation_history:
  print("{}: Area:{} {}^2 Perimeter: {} {}".format(item[0], item[1], units, item[2], units))
