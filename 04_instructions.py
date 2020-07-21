#Instructions

def instructions():
    print("****** Welcome to the Area Perimeter Calculator ******")

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