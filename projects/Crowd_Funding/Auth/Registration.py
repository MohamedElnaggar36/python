import re

import Home

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # regular exp for email


def checkEmail(email):
    if re.fullmatch(regex, email):  # method  from re lib
        return 1
    else:
        return 0


def checkData(firstName, lastName, email, password, phone):
    if len(firstName.strip()) == 0 or len(lastName.strip()) == 0 or len(password.strip()) == 0:
        print(" > all fields required !! ")
        return 0
    elif checkEmail(email) == 0:
        print("email is not valid..!")
        return 0
    elif len(password) < 4:
        print("Password is too short !!")
        return 0
    elif len(phone) < 10 or len(phone) > 11:
        print("enter a valid phone number..!")
        return 0
    else:
        return 1


def userRegister(firstName, lastName, email, password, phone):
    try:
        myUsers = open("Auth/users.txt", "a")
        userInfo = ":".join([firstName, lastName, email, password, phone])
        myUsers.writelines(f"{userInfo}\n")
        myUsers.close()
    except Exception as ex:
        print(f"error: {ex}")


def mainScreen():
    while True:

        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        email = input("User email: ")
        password = input("Password: ")
        confirmPass = input("Confirm Password: ")
        if password != confirmPass:
            print("Not matched password .. please try again")
        else:
            phone = input("Phone: ")
            if checkData(firstName, lastName, email, password, phone) != 0:
                userRegister(firstName, lastName, email, password, phone)
                print("Successfully Registered >>")
                Home.HomeApp()
                break
