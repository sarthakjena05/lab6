def encoder(password):
    global new_password
    new_digits = [(int(digit) + 3) % 10 for digit in password]
    new_password = "".join(map(str, new_digits))
    return new_password
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

#Nafiaz Chowdhury
def decoder(new_password):
    old_digits = [(int(digit) - 3) % 10 for digit in new_password]
    old_password = "".join(map(str, old_digits))
    return old_password

on = True
new_password_encoded = None

while on == True:

    menu()
    menu_option = input("Please enter an option:")

    if menu_option == "1":
        password = input("Please enter your password to encode:")
        enodoed = encoder(password)


    if menu_option == "3":
        on = False

    if menu_option == "2":
        if new_password_encoded == 0:
            print("Invalid")
        else:
            decode = decoder(enodoed)
            print(f"Encoded Password: {enodoed} Decoded:{decode}")

