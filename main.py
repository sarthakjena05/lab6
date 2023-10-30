def encoder(password):


    new_digits = [(int(digit) + 3) % 10 for digit in password]
    new_password = "".join(map(str, new_digits))
    return new_password


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")



on = True

while on == True:

    menu()
    menu_option = input("Please enter an option:")

    if menu_option == "1":
        password = input("Please enter your password to encode:")
        encoder(password)


    if menu_option == "3":
        on = False