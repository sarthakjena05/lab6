def encoder(password):
    new_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) if digit < '7' else str((int(digit) - 7)))
        new_password += encoded_digit
    return new_password
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

#Nafiaz Chowdhury


on = True
new_password_encoded = None

while on == True:

    menu()
    menu_option = input("Please enter an option:")

    if menu_option == "1":
        password = input("Please enter your password to encode:")
        enodoed = encoder(password)
        print("Your password has been encoded and stored")


    if menu_option == "3":
        on = False

    if menu_option == "2":
        if new_password_encoded == 0:
            print("Invalid")
        else:
            decode = decoder(enodoed)
            print(f"The Encoded Password: {enodoed} The Decoded Password:{decode}")




