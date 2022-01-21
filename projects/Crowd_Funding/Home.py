import Auth.Registration as rgstr
import Auth.Login as lgn
from projects.MainScreen import mainScreen


def HomeApp():
    print("<---------------- Welcome in Crowd Funing Application ---------------->")
    while True:
        userChoice = input("For Registration press 1, or login press 2: ")
        if userChoice == '1':
            print("Registration")
            rgstr.mainScreen()
            break
        elif userChoice == '2':
            lgn.mainLogin()
            break
        else:
            print("Try Again PLZ..")


def appScreen():
    mainScreen()


if __name__ == '__main__':
    HomeApp()
