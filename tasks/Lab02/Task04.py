import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # regular exp for email


def check(email):
    if re.fullmatch(regex, email):  # method  from re lib
        return 1
    else:
        return 0


def checkEmail(email):
    if email.find(".") != -1 and email.find("@") != -1 and len(email.strip()) != 0:
        return 1
    else:
        return 0


def myData(name, email):
    if len(name.strip()) != 0 and name.isnumeric() == False and checkEmail(email) != 0:
        print("Your Name is: " + name + " , Email is: " + email)
    else:
        print("Please Enter Valid Data !!")


myData("Mohamed", "Mohamed@gmail.com")