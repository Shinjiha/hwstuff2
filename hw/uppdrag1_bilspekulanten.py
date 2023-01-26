
print("Hello please write the description of thr cats in this format (Breed Color Age Gender) ex. Mainecoon Brown 6 Male")
a, b, c, d = input("Enter the info about the cat: ").split()

q = input ("Do want to add more cats? y/n")
if q == "y":
    e, f, g, h = input("Enter the info about the cat: ").split()
    print("..")
    n = input("which cat do you wanna see? 1-2")
    if n == "1":
        print("So you have a {}, With {} coloration, and its {} years old. And it's a {}".format(a, b, c, d))
        print()
    else:
        print("So you have a {}, With {} coloration, and its {} years old. And it's a {}".format(e, f, g, h))
        print()

else:
    print("So you have a {}, With {} coloration, and its {} years old. And it's a {}".format(a, b, c, d))
    print()


q = input("Do want to add more cats? y/n")
if q == "y":
    i, j, k, l = input("Enter the info about the cat: ").split()
    n = input("which cat do you wanna see? 1-3")
    if n == "1":
        print("So you have a {}, with {} coloration, and its {} years old. And it's a {}".format(a, b, c, d))
        print()

    elif n == "2":
        print("So you have a {}, with {} coloration, and its {} years old. And it's a {}".format(e, f, g, h))
        print()

    else:
        print("So you have a {}, with {} coloration, and its {} years old. And it's a {}".format(i, j, k, l))
        print()
else:
    n = input("which cat do you wanna see? 1-2")
    if n == "1":
        print("So you have a {}, with {} coloration, and its {} years old. And it's a {}".format(a, b, c, d))
        print()
    else:
        print("So you have a {}, with {} coloration, and its {} years old. And it's a {}".format(e, f, g, h))
        print()
