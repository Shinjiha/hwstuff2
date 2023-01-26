#center the text cuz why not
op1 = "1. Menu Option 1"
op2 = "2. Menu Option 2"
op3 = "3. Menu Option 3"
op4 = "3. Menu Option 3"
op5 = "5. Exit"
a = op1.center(50)
b = op2.center(50)
c = op3.center(50)
d = op4.center(50)
e = op5.center(50)


def print_menu():  ## design tm, fancy swanky
    print(2 * "･ﾟ ･ﾟ·:｡･ﾟﾟ･", "MENU", 2 * "･ﾟ ･ﾟ·:｡･ﾟﾟ･")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(3 * "☆⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆⋆ ͙͛☆ ˚₊⋆")


loop = True #true to keep it looping until you select 5/exit
while loop:
    print_menu()  ## Displays menu
    choice = input("Enter your choice [1-5]: ")

    if choice == "1":
        print("Menu 1 has been selected")

    elif choice == "2":
        print("Menu 2 has been selected")

    elif choice == "3":
        print("Menu 3 has been selected")

    elif choice == "4":
        print("Menu 4 has been selected")

    elif choice == "5":
        print("Menu 5 has been selected")

        loop = False  # Ends the loop and ends the code
    else:
        # anything other than the selected options wil lead to an error message
        input("Wrong option selection. Enter any key to try again..")
